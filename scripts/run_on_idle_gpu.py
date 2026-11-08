"""UUID で指定した空いている GPU 1 枚に限定してコマンドを起動する。"""

from contextlib import contextmanager
import fcntl
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET


class GPUUnavailable(RuntimeError):
    pass


def selected_uuid(environ):
    uuid = environ.get("CUDA_VISIBLE_DEVICES", "").strip()
    if not re.fullmatch(r"GPU-[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}", uuid):
        raise GPUUnavailable(
            "CUDA_VISIBLE_DEVICES に GPU の完全な UUID を 1 つだけ指定してください。"
            "番号・複数指定・未指定では起動しません。"
        )
    for name in ("WORLD_SIZE", "LOCAL_WORLD_SIZE"):
        try:
            size = int(environ.get(name, "1"))
        except ValueError as exc:
            raise GPUUnavailable(f"{name} の値を確認できません。") from exc
        if size != 1:
            raise GPUUnavailable("複数プロセスの分散実行は起動しません。必要なら事前に相談してください。")
    return uuid


def assert_idle(xml, uuid):
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as exc:
        raise GPUUnavailable("GPU の状態を解析できません。") from exc
    gpus = root.findall("gpu")
    if len(gpus) != 1 or gpus[0].findtext("uuid") != uuid:
        raise GPUUnavailable("取得した GPU と指定した UUID が一致しません。")
    gpu = gpus[0]
    processes = gpu.find("processes")
    if processes is None or (processes.text or "").strip() or len(processes):
        raise GPUUnavailable("実行中プロセスがあるか、プロセス情報を確認できません。")
    utilization = (gpu.findtext("utilization/gpu_util") or "").strip()
    if not re.fullmatch(r"0\s*%", utilization):
        raise GPUUnavailable(f"GPU が使用中か、使用率を確認できません（{utilization or '不明'}）。")
    # プロセス情報に現れない利用も疑い、ドライバの少量の基礎使用だけ許容する。
    memory = re.fullmatch(r"(\d+)\s+MiB", (gpu.findtext("fb_memory_usage/used") or "").strip())
    if memory is None or int(memory.group(1)) > 16:
        raise GPUUnavailable("GPU メモリ使用量が 16 MiB を超えるか、使用量を確認できません。")


def cpu_limits(environ):
    result = dict(environ)
    for name in (
        "OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS",
        "NUMEXPR_NUM_THREADS", "RAYON_NUM_THREADS", "MAX_JOBS",
    ):
        result.setdefault(name, "2")
    result.setdefault("TOKENIZERS_PARALLELISM", "false")
    return result


@contextmanager
def idle_gpu():
    uuid = selected_uuid(os.environ)
    # 自分のガード経由の同時起動を抑える協調ロック。他ユーザーの予約にはならない。
    lock_path = Path(tempfile.gettempdir()) / f"wan-gpu-{os.getuid()}-{uuid}.lock"
    with lock_path.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise GPUUnavailable("同じ GPU で自分の別のガード付き実行が進行中です。") from exc
        try:
            state = subprocess.run(
                ["nvidia-smi", "-q", "-x", "-i", uuid],
                check=True, capture_output=True, text=True, timeout=10,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            raise GPUUnavailable("nvidia-smi で GPU の空きを確認できません。") from exc
        assert_idle(state.stdout, uuid)
        environment = cpu_limits(os.environ)
        environment["CUDA_VISIBLE_DEVICES"] = uuid
        os.set_inheritable(lock.fileno(), True)
        print(f"起動前確認済み：{uuid} の 1 枚のみを使用します。", file=sys.stderr, flush=True)
        yield environment


def main(argv=None):
    command = list(sys.argv[1:] if argv is None else argv)
    if command[:1] == ["--"]:
        command.pop(0)
    if not command:
        print("Usage: run_on_idle_gpu.py -- <command> [args ...]", file=sys.stderr)
        return 2
    try:
        with idle_gpu() as environment:
            os.execvpe(command[0], command, environment)
    except (GPUUnavailable, OSError) as exc:
        print(f"起動を中止しました：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
