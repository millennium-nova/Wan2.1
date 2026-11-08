"""GPU を使用せず、起動拒否と単一 UUID の引き継ぎを検証する。"""

import contextlib
import io
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_environment
import run_on_idle_gpu as guard

UUID = "GPU-12345678-1234-1234-1234-123456789abc"


def snapshot(processes="", utilization="0 %", memory="1 MiB", uuid=UUID):
    return (
        f"<nvidia_smi_log><gpu><uuid>{uuid}</uuid>"
        f"<processes>{processes}</processes>"
        f"<utilization><gpu_util>{utilization}</gpu_util></utilization>"
        f"<fb_memory_usage><used>{memory}</used></fb_memory_usage>"
        "</gpu></nvidia_smi_log>"
    )


class GPUGuardTests(unittest.TestCase):
    def test_only_one_full_uuid_is_accepted(self):
        for selection in ("", "0", "0,1", f"{UUID},{UUID}", "GPU-12345678"):
            with self.subTest(selection=selection), self.assertRaises(guard.GPUUnavailable):
                guard.selected_uuid({"CUDA_VISIBLE_DEVICES": selection})
        self.assertEqual(guard.selected_uuid({"CUDA_VISIBLE_DEVICES": UUID}), UUID)
        with self.assertRaises(guard.GPUUnavailable):
            guard.selected_uuid({"CUDA_VISIBLE_DEVICES": UUID, "WORLD_SIZE": "2"})

    def test_any_process_blocks_launch_even_at_zero_utilization(self):
        for kind in ("C", "G", "M", "O"):
            xml = snapshot(processes=f"<process_info><pid>999</pid><type>{kind}</type></process_info>")
            with self.subTest(kind=kind), self.assertRaises(guard.GPUUnavailable):
                guard.assert_idle(xml, UUID)

    def test_unknown_or_busy_state_is_rejected(self):
        states = (
            snapshot(processes="N/A"), snapshot(processes="Unidentified processes found"),
            snapshot(utilization="1 %"), snapshot(utilization="N/A"),
            snapshot(memory="100 MiB"), snapshot(memory="N/A"),
            snapshot(uuid="GPU-other"), "not XML", "<nvidia_smi_log/>",
            snapshot().replace("<processes></processes>", ""),
        )
        for xml in states:
            with self.subTest(xml=xml), self.assertRaises(guard.GPUUnavailable):
                guard.assert_idle(xml, UUID)

    def test_busy_gpu_never_starts_child(self):
        state = subprocess.CompletedProcess([], 0, snapshot(processes="<process_info/>"), "")
        with patch.dict(os.environ, {"CUDA_VISIBLE_DEVICES": UUID}, clear=True), \
                patch.object(guard.subprocess, "run", return_value=state), \
                patch.object(guard.os, "execvpe") as launch, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(guard.main(["python", "experiment.py"]), 1)
            launch.assert_not_called()

    def test_failed_query_never_starts_child(self):
        with patch.dict(os.environ, {"CUDA_VISIBLE_DEVICES": UUID}, clear=True), \
                patch.object(guard.subprocess, "run", side_effect=FileNotFoundError), \
                patch.object(guard.os, "execvpe") as launch, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(guard.main(["python", "experiment.py"]), 1)
            launch.assert_not_called()

    def test_idle_gpu_limits_child_and_blocks_duplicate_launch(self):
        state = subprocess.CompletedProcess([], 0, snapshot(), "")
        with patch.dict(os.environ, {"CUDA_VISIBLE_DEVICES": UUID}, clear=True), \
                patch.object(guard.subprocess, "run", return_value=state) as query, \
                contextlib.redirect_stderr(io.StringIO()):
            with guard.idle_gpu() as environment:
                self.assertEqual(environment["CUDA_VISIBLE_DEVICES"], UUID)
                self.assertEqual(environment["OMP_NUM_THREADS"], "2")
                self.assertEqual(environment["OPENBLAS_NUM_THREADS"], "2")
                with self.assertRaises(guard.GPUUnavailable):
                    with guard.idle_gpu():
                        self.fail("同じ GPU の同時起動が許可された")
            query.assert_called_once()
            self.assertEqual(query.call_args.args[0], ["nvidia-smi", "-q", "-x", "-i", UUID])
            # ロックは確認終了後に再利用できる。
            with guard.idle_gpu():
                pass

    def test_check_rejects_before_importing_gpu_packages(self):
        with patch.dict(os.environ, {}, clear=True), \
                patch.object(sys, "argv", ["check_environment.py"]), \
                patch.object(check_environment, "check_packages") as check, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(check_environment.main(), 1)
            check.assert_not_called()

    def test_cpu_check_hides_all_gpus_before_import(self):
        def check(*, cpu):
            self.assertTrue(cpu)
            self.assertEqual(os.environ["CUDA_VISIBLE_DEVICES"], "")
            self.assertEqual(os.environ["MKL_NUM_THREADS"], "2")

        with patch.dict(os.environ, {"CUDA_VISIBLE_DEVICES": UUID}, clear=True), \
                patch.object(sys, "argv", ["check_environment.py", "--cpu"]), \
                patch.object(check_environment, "check_packages", side_effect=check):
            self.assertEqual(check_environment.main(), 0)


if __name__ == "__main__":
    unittest.main()
