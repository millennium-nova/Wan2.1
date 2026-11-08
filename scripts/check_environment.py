"""モデルの重みをダウンロードせず、実験環境の依存関係と GPU を確認する。"""

import argparse
import importlib
import importlib.metadata
import os
import shutil
import sys

from run_on_idle_gpu import GPUUnavailable, cpu_limits, idle_gpu


def check_packages(cpu):
    import torch

    packages = {
        "torch": "torch",
        "torchvision": "torchvision",
        "flash_attn": "flash-attn",
        "cv2": "opencv-python",
        "diffusers": "diffusers",
        "transformers": "transformers",
        "tokenizers": "tokenizers",
        "accelerate": "accelerate",
        "tqdm": "tqdm",
        "imageio": "imageio",
        "easydict": "easydict",
        "ftfy": "ftfy",
        "dashscope": "dashscope",
        "imageio_ffmpeg": "imageio-ffmpeg",
        "gradio": "gradio",
        "numpy": "numpy",
        "huggingface_hub": "huggingface-hub",
        "decord": "decord",
    }
    print(f"Python: {sys.version.split()[0]}")
    for module, distribution in packages.items():
        importlib.import_module(module)
        print(f"{distribution}: {importlib.metadata.version(distribution)}")

    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg が見つかりません。pixi run check で実行してください。")
    print(f"PyTorch CUDA runtime: {torch.version.cuda}")
    if cpu:
        print("依存関係の読み込みは成功しました。")
        print("CPU 確認のため、GPU 初期化を伴う wan の import と CUDA 実行は省略しました。")
        return
    if not torch.cuda.is_available() or torch.cuda.device_count() != 1:
        raise GPUUnavailable("PyTorch から指定した GPU 1 枚だけを利用できる状態ではありません。")

    import wan
    from wan.modules.attention import flash_attention

    print(f"wan: {importlib.metadata.version('wan')} ({wan.__file__})")
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    q = torch.randn(1, 16, 2, 32, device="cuda", dtype=torch.float16)
    result = flash_attention(q, q, q, dtype=torch.float16, version=2)
    torch.cuda.synchronize()
    if result.shape != q.shape or not torch.isfinite(result).all().item():
        raise RuntimeError("FlashAttention の実行結果が不正です。")
    print("CUDA / FlashAttention の実行に成功しました。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpu", action="store_true", help="GPU を使わず依存関係だけ確認する")
    args = parser.parse_args()
    if args.cpu:
        os.environ.update(cpu_limits(os.environ))
        os.environ["CUDA_VISIBLE_DEVICES"] = ""
        check_packages(cpu=True)
        return 0
    try:
        # torch / wan の import より前に空きを検査し、確認計算の終了までロックする。
        with idle_gpu() as environment:
            os.environ.update(environment)
            check_packages(cpu=False)
    except (GPUUnavailable, OSError) as exc:
        print(f"確認を中止しました：{exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
