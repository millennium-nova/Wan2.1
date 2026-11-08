# Wan2.1

<p align="center">
    <img src="assets/logo.png" width="400"/>
<p>

<p align="center">
    💜 <a href="https://wan.video"><b>Wan</b></a> &nbsp&nbsp ｜ &nbsp&nbsp 🖥️ <a href="https://github.com/Wan-Video/Wan2.1">GitHub</a> &nbsp&nbsp  | &nbsp&nbsp🤗 <a href="https://huggingface.co/Wan-AI/">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/Wan-AI">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2503.20314">技術レポート</a> &nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://wan.video/welcome?spm=a2ty_o02.30011076.0.0.6c9ee41eCcluqg">ブログ</a> &nbsp&nbsp | &nbsp&nbsp💬 <a href="https://gw.alicdn.com/imgextra/i2/O1CN01tqjWFi1ByuyehkTSB_!!6000000000015-0-tps-611-1279.jpg">WeChat グループ</a>&nbsp&nbsp | &nbsp&nbsp 📖 <a href="https://discord.gg/AKNgpMK4Yj">Discord</a>&nbsp&nbsp
<br>

-----

[**Wan：オープンで先進的な大規模動画生成モデル**](https://arxiv.org/abs/2503.20314) <be>

このリポジトリでは、動画生成の可能性を広げる、包括的でオープンな動画基盤モデル群 **Wan2.1** を公開しています。主な特徴は次のとおりです。
- 👍 **最先端の性能**：**Wan2.1** は複数のベンチマークで、既存のオープンソースモデルや最先端の商用サービスを一貫して上回る性能を発揮します。
- 👍 **一般向け GPU に対応**：T2V-1.3B モデルに必要な VRAM はわずか 8.19 GB で、ほぼすべての一般向け GPU で動作します。RTX 4090 では、量子化などの最適化を使わずに、5 秒間の 480P 動画を約 4 分で生成できます。一部のクローズドソースモデルにも匹敵する性能を備えています。
- 👍 **多様なタスクに対応**：**Wan2.1** は、テキストからの動画生成、画像からの動画生成、動画編集、テキストからの画像生成、動画からの音声生成で優れた性能を発揮し、動画生成分野の発展に貢献します。
- 👍 **動画内の文字生成**：**Wan2.1** は、中国語と英語の両方の文字を生成できる初の動画モデルです。安定した文字生成により、実用の幅が広がります。
- 👍 **高性能な動画 VAE**：**Wan-VAE** は高い効率と性能を備え、時間方向の情報を保持しながら、長さに制限なく 1080P 動画をエンコード・デコードできます。動画・画像生成の基盤として最適です。

## デモ動画

<div align="center">
  <video src="https://github.com/user-attachments/assets/4aca6063-60bf-4953-bfb7-e265053f49ef" width="70%" poster=""> </video>
</div>

## 🔥 最新情報

* 2025年5月14日：👋 動画の制作と編集を一つでこなす **Wan2.1** [VACE](https://github.com/ali-vilab/VACE) を公開しました。[推論コード](#run-vace)、[重み](#model-download)、[技術レポート](https://arxiv.org/abs/2503.07598)もあわせて公開しています！
* 2025年4月17日：👋 **Wan2.1** [FLF2V](#run-first-last-frame-to-video-generation) の推論コードと重みを公開しました！
* 2025年3月21日：👋 **Wan2.1** の[技術レポート](https://files.alicdn.com/tpsservice/5c9de1c74de03972b7aa657e5a54756b.pdf)を公開しました。ご意見やフィードバックをお待ちしています！
* 2025年3月3日：👋 **Wan2.1** の T2V と I2V が Diffusers に統合されました（[T2V](https://huggingface.co/docs/diffusers/main/en/api/pipelines/wan#diffusers.WanPipeline) | [I2V](https://huggingface.co/docs/diffusers/main/en/api/pipelines/wan#diffusers.WanImageToVideoPipeline)）。ぜひお試しください！
* 2025年2月27日：👋 **Wan2.1** が [ComfyUI](https://comfyanonymous.github.io/ComfyUI_examples/wan/) に統合されました。ぜひご活用ください！
* 2025年2月25日：👋 **Wan2.1** の推論コードと重みを公開しました。

## コミュニティの取り組み
**Wan2.1** を改良した成果をより多くの方に紹介したい場合は、ぜひお知らせください。
- [Helios](https://github.com/PKU-YuanGroup/Helios) は、**Wan2.1** をベースにした画期的な動画生成モデルです。従来の長時間動画におけるドリフト抑制手法や一般的な高速化手法に頼らず、H100 GPU 1 基で 19.5 FPS（Ascend NPU 1 基では約 10 FPS）の速度で、数分規模の高品質な動画を生成できます。詳しくは[プロジェクトページ](https://pku-yuangroup.github.io/Helios-Page/)をご覧ください。
- [Video-As-Prompt](https://github.com/bytedance/Video-As-Prompt) は、**Wan2.1-14B-I2V** をベースに、Mixture-of-Transformers アーキテクチャとコンテキスト内の制御（概念、スタイル、動き、カメラなど）を組み合わせた、初の統合型セマンティック制御動画生成モデルです。作例は[プロジェクトページ](https://bytedance.github.io/Video-As-Prompt/)をご覧ください。
- [LightX2V](https://github.com/ModelTC/LightX2V) は、**Wan2.1** と **Wan2.2** を統合した、軽量で効率的な動画生成フレームワークです。複数の実装上の高速化手法に対応し、RTX 5090 や RTX 4060（VRAM 8 GB）で高速な推論を実行できます。
- [DriVerse](https://github.com/shalfun/DriVerse) は、**Wan2.1-14B-I2V** をベースにした自動運転向け世界モデルです。任意のシーンのフレームと指定した走行軌跡を条件に、その後の走行動画を生成します。作例は[プロジェクトページ](https://github.com/shalfun/DriVerse/tree/main)をご覧ください。
- [Training-Free-WAN-Editing](https://github.com/KyujinHan/Awesome-Training-Free-WAN2.1-Editing) は、**Wan2.1-T2V-1.3B** をベースに、[FlowEdit](https://arxiv.org/abs/2412.08629) や [FlowAlign](https://arxiv.org/abs/2505.23145) など、画像向けの追加学習不要な手法を用いて、追加学習なしで動画を編集できます。
- [Wan-Move](https://github.com/ali-vilab/Wan-Move) は、NeurIPS 2025 に採択されたフレームワークです。**Wan2.1-I2V-14B** で、最先端のきめ細かな点単位の動作制御を実現します。詳しくは[プロジェクトページ](https://wan-move.github.io/)をご覧ください。
- [EchoShot](https://github.com/JoHnneyWang/EchoShot) は、**Wan2.1-T2V-1.3B** をベースにした、複数ショットの人物動画生成に対応するモデルです。同じ人物が登場する複数の動画クリップを生成でき、内容も柔軟に制御できます。詳しくは[プロジェクトページ](https://johnneywang.github.io/EchoShot-webpage/)をご覧ください。
- [AniCrafter](https://github.com/MyNiuuu/AniCrafter) は、**Wan2.1-14B-I2V** をベースにした人物アニメーションモデルです。3DGS アバターで動画拡散モデルを制御し、任意の人物を任意のシーンに配置して、指定した動作シーケンスに沿って動かせます。作例は[プロジェクトページ](https://myniuuu.github.io/AniCrafter)をご覧ください。
- [HyperMotion](https://vivocameraresearch.github.io/hypermotion/) は、**Wan2.1** をベースに人物画像をアニメーション化するフレームワークです。ポーズに基づくアニメーションで、複雑な身体動作を生成する課題に取り組んでいます。作例は[ウェブサイト](https://vivocameraresearch.github.io/magictryon/)をご覧ください。
- [MagicTryOn](https://vivocameraresearch.github.io/magictryon/) は、**Wan2.1-14B-I2V** をベースにした動画バーチャル試着フレームワークです。衣服の細部の表現や、人物が動いた際の見た目の安定性に関する、既存モデルの課題に取り組んでいます。作例は[ウェブサイト](https://vivocameraresearch.github.io/magictryon/)をご覧ください。
- [ATI](https://github.com/bytedance/ATI) は、**Wan2.1-I2V-14B** をベースに、軌跡を使って動きを制御するフレームワークです。動画生成における物体の動き、局所的な動き、カメラの動きを統一的に制御できます。作例は[ウェブサイト](https://anytraj.github.io/)をご覧ください。
- [Phantom](https://github.com/Phantom-video/Phantom) は、**Wan2.1-T2V-1.3B** と **Wan2.1-T2V-14B** をベースに、単一または複数の被写体の参照画像に対応する統合型動画生成フレームワークを開発しています。[作例](https://github.com/Phantom-video/Phantom)をご覧ください。
- [UniAnimate-DiT](https://github.com/ali-vilab/UniAnimate-DiT) は、**Wan2.1-14B-I2V** をベースに人物画像をアニメーション化するモデルを学習し、推論コードと学習コードを公開しています。ぜひお試しください！
- [CFG-Zero](https://github.com/WeichenFan/CFG-Zero-star) は、CFG の観点から **Wan2.1** の T2V・I2V 両モデルを改良しています。
- [TeaCache](https://github.com/ali-vilab/TeaCache) が **Wan2.1** の高速化に対応しました。約 2 倍の高速化が可能です。ぜひお試しください！
- [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) は、動画からの動画生成、FP8 量子化、VRAM の最適化、LoRA 学習など、**Wan2.1** 向けの機能を幅広く提供しています。[使用例](https://github.com/modelscope/DiffSynth-Studio/tree/main/examples/wanvideo)をご覧ください。


## 📑 開発予定と対応状況
- Wan2.1 テキストからの動画生成（Text-to-Video）
    - [x] 14B・1.3B モデルの複数 GPU 向け推論コード
    - [x] 14B・1.3B モデルのチェックポイント
    - [x] Gradio デモ
    - [x] ComfyUI との統合
    - [x] Diffusers との統合
    - [ ] Diffusers での複数 GPU 推論
- Wan2.1 画像からの動画生成（Image-to-Video）
    - [x] 14B モデルの複数 GPU 向け推論コード
    - [x] 14B モデルのチェックポイント
    - [x] Gradio デモ
    - [x] ComfyUI との統合
    - [x] Diffusers との統合
    - [ ] Diffusers での複数 GPU 推論
- Wan2.1 開始・終了フレームからの動画生成（First-Last-Frame-to-Video）
    - [x] 14B モデルの複数 GPU 向け推論コード
    - [x] 14B モデルのチェックポイント
    - [x] Gradio デモ
    - [ ] ComfyUI との統合
    - [ ] Diffusers との統合
    - [ ] Diffusers での複数 GPU 推論
- Wan2.1 VACE
    - [x] 14B・1.3B モデルの複数 GPU 向け推論コード
    - [x] 14B・1.3B モデルのチェックポイント
    - [x] Gradio デモ
    - [x] ComfyUI との統合
    - [ ] Diffusers との統合
    - [ ] Diffusers での複数 GPU 推論

## クイックスタート

#### インストール

##### Pixi を使う場合（実験用）

このリポジトリには、Linux x86_64 の NVIDIA GPU 向けに `pixi.toml` と `pixi.lock` を用意しています。Pixi 0.66.0 以降で、次のコマンドを実行してください。

```sh
pixi install --locked
pixi run check-cpu
```

環境はリポジトリ内の `.pixi/envs/default` に作成されます。既存の `pyproject.toml` に定義された依存関係を読み込み、Wan 自体は編集可能な状態でインストールするため、ソースコードの変更がそのまま反映されます。`requirements.txt` を別途インストールする必要はありません。

GPU ノードを使う場合は、SSH でログインしてから同じリポジトリで実行します。他ユーザーのプロセスが動いている GPU は、空き VRAM があっても使用しないでください。実行直前にプロセスの有無を確認し、空いていて利用を許可された GPU の完全な UUID を `CUDA_VISIBLE_DEVICES` に 1 つだけ指定します。GPU の UUID を指定すると、`nvidia-smi` と CUDA のデバイス番号の違いを避けられます。

```sh
ssh npalgpu02
cd /home/kazhigo/repos/Wan2.1
nvidia-smi --query-gpu=index,uuid,name,memory.used --format=csv
nvidia-smi  # GPU ごとのプロセスを確認する
export CUDA_VISIBLE_DEVICES=GPU-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  # 空いている GPU 1 枚の UUID
pixi run check
```

`pixi run check` と `pixi run generate` は GPU 初期化前に状態を検査し、UUID の未指定・複数指定、既存プロセスあり、使用率が 0% 以外、メモリ使用量が 16 MiB 超、状態取得の失敗の場合には起動しません。同じ GPU に自分のガード付き実行を重ねないための協調ロックも使用します。ただし、これは他ユーザーに対する GPU の予約ではありません。サーバーの割当・予約ルールがある場合は従ってください。

Python 3.11、PyTorch 2.8.0（CUDA 12.8）、torchvision 0.23.0、FlashAttention 2.8.3 を組み合わせ、対応する公式バイナリを使用します。CUDA Toolkit の手動インストールや FlashAttention のローカルビルドは不要ですが、動画生成には対応する NVIDIA GPU とドライバが必要です。`pixi run check` は Wan の読み込みと小さな FlashAttention の計算まで確認します。GPU を使用しない依存確認には `pixi run check-cpu` を使ってください。このコードの動画生成処理は CUDA を前提としているため、CPU のみでの生成には対応していません。

モデルのダウンロードと生成は、たとえば次のように実行できます。

```sh
pixi run download Wan-AI/Wan2.1-T2V-1.3B --local-dir ./Wan2.1-T2V-1.3B
pixi run generate --task t2v-1.3B --size '832*480' --ckpt_dir ./Wan2.1-T2V-1.3B --offload_model True --t5_cpu --sample_shift 8 --sample_guide_scale 6 --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."
```

対話的に作業する場合は `pixi shell` を使ってください。GPU を使う任意のスクリプトには `pixi run gpu-run -- python your_script.py` を使い、同じ起動前チェックを適用できます。ガード経由の実行と CPU 確認では、OpenMP・BLAS などのスレッド数と `MAX_JOBS` の未設定時の既定値を 2 に抑えます。データローダーの worker 数、動画変換、ダウンロードの並列数も控えめにし、共有ストレージへの大量・反復 I/O は避けてください。

実験は原則として 1 回につき GPU 1 枚で行い、どうしても複数枚必要な場合は事前に相談してください。他人のプロセスを停止して空きを作ったり、必要な実験がないのに GPU を確保し続けたりしないでください。以降の複数 GPU の例は上流の機能説明であり、共有サーバーで無断実行してよいという意味ではありません。モデルの重みは環境の作成時にはダウンロードしません。複数 GPU 用の `xfuser` はこの環境に含まれていません。

配布元と環境設定の詳細は、[Pixi の PyTorch ガイド](https://pixi.prefix.dev/latest/python/pytorch/)、[PyTorch のバージョン別インストール手順](https://pytorch.org/get-started/previous-versions/)、[FlashAttention の公式リリース](https://github.com/Dao-AILab/flash-attention/releases/tag/v2.8.3)をご覧ください。

##### pip を使う場合

リポジトリをクローンします。
```sh
git clone https://github.com/Wan-Video/Wan2.1.git
cd Wan2.1
```

依存パッケージをインストールします。
```sh
# torch が 2.4.0 以上であることを確認してください
pip install -r requirements.txt
```


<a id="model-download"></a>

#### モデルのダウンロード

| モデル       | ダウンロードリンク                                                                                                                                           |    備考                      |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| T2V-14B      | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B)      🤖 [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-T2V-14B)             | 480P・720P に対応
| I2V-14B-720P | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-720P)    🤖 [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-I2V-14B-720P)     | 720P に対応
| I2V-14B-480P | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P)    🤖 [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-I2V-14B-480P)     | 480P に対応
| T2V-1.3B     | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B)     🤖 [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-T2V-1.3B)            | 480P に対応
| FLF2V-14B    | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-FLF2V-14B-720P)     🤖 [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-FLF2V-14B-720P) | 720P に対応
| VACE-1.3B    | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B)     🤖 [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-VACE-1.3B)          | 480P に対応
| VACE-14B     | 🤗 [Huggingface](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)     🤖 [ModelScope](https://www.modelscope.cn/models/Wan-AI/Wan2.1-VACE-14B)        | 480P・720P に対応

> 💡補足：
> * 1.3B モデルは 720P 解像度の動画も生成できます。ただし、この解像度での学習が限られているため、480P と比べると生成結果が不安定になる傾向があります。より良い結果を得るには、480P の使用をおすすめします。
> * 開始・終了フレームからの動画生成モデルは、主に中国語のテキストと動画のペアで学習しています。そのため、より良い結果を得るには、中国語のプロンプトをおすすめします。


huggingface-cli でモデルをダウンロードする場合：
``` sh
pip install "huggingface_hub[cli]"
huggingface-cli download Wan-AI/Wan2.1-T2V-14B --local-dir ./Wan2.1-T2V-14B
```

modelscope-cli でモデルをダウンロードする場合：
``` sh
pip install modelscope
modelscope download Wan-AI/Wan2.1-T2V-14B --local_dir ./Wan2.1-T2V-14B
```
#### テキストからの動画生成

このリポジトリは、2 種類のテキスト動画生成モデル（1.3B と 14B）と、2 種類の解像度（480P と 720P）に対応しています。各モデルの対応状況は次のとおりです。

<table>
    <thead>
        <tr>
            <th rowspan="2">タスク</th>
            <th colspan="2">解像度</th>
            <th rowspan="2">モデル</th>
        </tr>
        <tr>
            <th>480P</th>
            <th>720P</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>t2v-14B</td>
            <td style="color: green;">✔️</td>
            <td style="color: green;">✔️</td>
            <td>Wan2.1-T2V-14B</td>
        </tr>
        <tr>
            <td>t2v-1.3B</td>
            <td style="color: green;">✔️</td>
            <td style="color: red;">❌</td>
            <td>Wan2.1-T2V-1.3B</td>
        </tr>
    </tbody>
</table>


##### (1) プロンプト拡張を使わない場合

まずは実行しやすいように、[プロンプト拡張](#2-using-prompt-extention)を省いた基本的な推論手順から説明します。

- 単一 GPU での推論

``` sh
python generate.py  --task t2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-T2V-14B --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."
```

OOM（メモリ不足）が発生する場合は、`--offload_model True` と `--t5_cpu` オプションで GPU メモリの使用量を減らせます。たとえば、RTX 4090 では次のように実行します。

``` sh
python generate.py  --task t2v-1.3B --size 832*480 --ckpt_dir ./Wan2.1-T2V-1.3B --offload_model True --t5_cpu --sample_shift 8 --sample_guide_scale 6 --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."
```

> 💡補足：`T2V-1.3B` モデルでは、`--sample_guide_scale 6` の設定をおすすめします。`--sample_shift` は、生成結果に応じて 8〜12 の範囲で調整できます。


- FSDP + xDiT USP を使った複数 GPU での推論

  FSDP と [xDiT](https://github.com/xdit-project/xDiT) USP を使って推論を高速化します。

  * Ulysses 方式

    [`Ulysses`](https://arxiv.org/abs/2309.14509) 方式を使う場合は、`--ulysses_size $GPU_NUMS` を設定してください。`num_heads` は `ulysses_size` で割り切れる必要があります。1.3B モデルの `num_heads` は `12` で、一般的な複数 GPU マシンの GPU 数である 8 では割り切れないため、`Ring` 方式をおすすめします。

  * Ring 方式

    [`Ring`](https://arxiv.org/pdf/2310.01889) 方式を使う場合は、`--ring_size $GPU_NUMS` を設定してください。この方式では、シーケンス長が `ring_size` で割り切れる必要があります。

  `Ulysses` と `Ring` を組み合わせることもできます。


``` sh
pip install "xfuser>=0.4.1"
torchrun --nproc_per_node=8 generate.py --task t2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-T2V-14B --dit_fsdp --t5_fsdp --ulysses_size 8 --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage."
```


<a id="2-using-prompt-extention"></a>
<a id="2-using-prompt-extension"></a>

##### (2) プロンプト拡張を使う場合

プロンプトを拡張すると、生成動画の細部が充実し、品質の向上につながります。そのため、プロンプト拡張を有効にすることをおすすめします。次の 2 つの方法を利用できます。

- Dashscope API で拡張する
  - 事前に `dashscope.api_key` を取得してください（[英語](https://www.alibabacloud.com/help/en/model-studio/getting-started/first-api-call-to-qwen) | [中国語](https://help.aliyun.com/zh/model-studio/getting-started/first-api-call-to-qwen)）。
  - 環境変数 `DASH_API_KEY` に Dashscope の API キーを設定してください。Alibaba Cloud の国際サイトを利用する場合は、環境変数 `DASH_API_URL` に `https://dashscope-intl.aliyuncs.com/api/v1` も設定する必要があります。詳しい手順は [Dashscope のドキュメント](https://www.alibabacloud.com/help/en/model-studio/developer-reference/use-qwen-by-calling-api?spm=a2c63.p38356.0.i1)をご覧ください。
  - テキストからの動画生成には `qwen-plus`、画像からの動画生成には `qwen-vl-max` を使用します。
  - 拡張に使うモデルは `--prompt_extend_model` で変更できます。実行例は次のとおりです。
```sh
DASH_API_KEY=your_key python generate.py  --task t2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-T2V-14B --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage" --use_prompt_extend --prompt_extend_method 'dashscope' --prompt_extend_target_lang 'zh'
```

- ローカルモデルで拡張する

  - デフォルトでは Hugging Face 上の Qwen モデルを使います。利用可能な GPU メモリに応じて、Qwen やその他のモデルを選択できます。
  - テキストからの動画生成には、`Qwen/Qwen2.5-14B-Instruct`、`Qwen/Qwen2.5-7B-Instruct`、`Qwen/Qwen2.5-3B-Instruct` などを利用できます。
  - 画像、または開始・終了フレームからの動画生成には、`Qwen/Qwen2.5-VL-7B-Instruct`、`Qwen/Qwen2.5-VL-3B-Instruct` などを利用できます。
  - 一般に、大きなモデルほど拡張結果が良くなりますが、より多くの GPU メモリが必要です。
  - 拡張に使うモデルは `--prompt_extend_model` で変更できます。ローカルモデルのパス、または Hugging Face のモデル名を指定してください。実行例は次のとおりです。

``` sh
python generate.py  --task t2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-T2V-14B --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage" --use_prompt_extend --prompt_extend_method 'local_qwen' --prompt_extend_target_lang 'zh'
```


##### (3) Diffusers で実行する場合

次のコードで、Diffusers を使って **Wan2.1**-T2V の推論を簡単に実行できます。
``` python
import torch
from diffusers.utils import export_to_video
from diffusers import AutoencoderKLWan, WanPipeline
from diffusers.schedulers.scheduling_unipc_multistep import UniPCMultistepScheduler

# 利用可能なモデル： Wan-AI/Wan2.1-T2V-14B-Diffusers, Wan-AI/Wan2.1-T2V-1.3B-Diffusers
model_id = "Wan-AI/Wan2.1-T2V-14B-Diffusers"
vae = AutoencoderKLWan.from_pretrained(model_id, subfolder="vae", torch_dtype=torch.float32)
flow_shift = 5.0 # 720P では 5.0、480P では 3.0
scheduler = UniPCMultistepScheduler(prediction_type='flow_prediction', use_flow_sigmas=True, num_train_timesteps=1000, flow_shift=flow_shift)
pipe = WanPipeline.from_pretrained(model_id, vae=vae, torch_dtype=torch.bfloat16)
pipe.scheduler = scheduler
pipe.to("cuda")

prompt = "A cat and a dog baking a cake together in a kitchen. The cat is carefully measuring flour, while the dog is stirring the batter with a wooden spoon. The kitchen is cozy, with sunlight streaming through the window."
negative_prompt = "Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, images, static, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards"

output = pipe(
     prompt=prompt,
     negative_prompt=negative_prompt,
     height=720,
     width=1280,
     num_frames=81,
     guidance_scale=5.0,
    ).frames[0]
export_to_video(output, "output.mp4", fps=16)
```
> 💡補足：この例には、プロンプト拡張と分散推論は含まれていません。プロンプト拡張と複数 GPU に対応した Diffusers 版を近日中に公開する予定です。


##### (4) ローカルで Gradio を実行する場合

``` sh
cd gradio
# Dashscope API でプロンプトを拡張する場合
DASH_API_KEY=your_key python t2v_14B_singleGPU.py --prompt_extend_method 'dashscope' --ckpt_dir ./Wan2.1-T2V-14B

# ローカルモデルでプロンプトを拡張する場合
python t2v_14B_singleGPU.py --prompt_extend_method 'local_qwen' --ckpt_dir ./Wan2.1-T2V-14B
```



#### 画像からの動画生成

テキストからの動画生成と同様に、画像からの動画生成も、プロンプト拡張を使う場合と使わない場合に分けて説明します。各モデルの対応状況は次のとおりです。
<table>
    <thead>
        <tr>
            <th rowspan="2">タスク</th>
            <th colspan="2">解像度</th>
            <th rowspan="2">モデル</th>
        </tr>
        <tr>
            <th>480P</th>
            <th>720P</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>i2v-14B</td>
            <td style="color: green;">❌</td>
            <td style="color: green;">✔️</td>
            <td>Wan2.1-I2V-14B-720P</td>
        </tr>
        <tr>
            <td>i2v-14B</td>
            <td style="color: green;">✔️</td>
            <td style="color: red;">❌</td>
            <td>Wan2.1-T2V-14B-480P</td>
        </tr>
    </tbody>
</table>


##### (1) プロンプト拡張を使わない場合

- 単一 GPU での推論
```sh
python generate.py --task i2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-I2V-14B-720P --image examples/i2v_input.JPG --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside."
```

> 💡画像からの動画生成では、`size` は生成動画の面積（総画素数）を指定します。アスペクト比は入力画像に合わせて決まります。


- FSDP + xDiT USP を使った複数 GPU での推論

```sh
pip install "xfuser>=0.4.1"
torchrun --nproc_per_node=8 generate.py --task i2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-I2V-14B-720P --image examples/i2v_input.JPG --dit_fsdp --t5_fsdp --ulysses_size 8 --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside."
```

##### (2) プロンプト拡張を使う場合


プロンプト拡張の手順は、[こちら](#2-using-prompt-extention)をご覧ください。

`Qwen/Qwen2.5-VL-7B-Instruct` によるローカルのプロンプト拡張を使う場合：
```
python generate.py --task i2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-I2V-14B-720P --image examples/i2v_input.JPG --use_prompt_extend --prompt_extend_model Qwen/Qwen2.5-VL-7B-Instruct --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside."
```

`dashscope` によるリモートのプロンプト拡張を使う場合：
```
DASH_API_KEY=your_key python generate.py --task i2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-I2V-14B-720P --image examples/i2v_input.JPG --use_prompt_extend --prompt_extend_method 'dashscope' --prompt "Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard. The fluffy-furred feline gazes directly at the camera with a relaxed expression. Blurred beach scenery forms the background featuring crystal-clear waters, distant green hills, and a blue sky dotted with white clouds. The cat assumes a naturally relaxed posture, as if savoring the sea breeze and warm sunlight. A close-up shot highlights the feline's intricate details and the refreshing atmosphere of the seaside."
```


##### (3) Diffusers で実行する場合

次のコードで、Diffusers を使って **Wan2.1**-I2V の推論を簡単に実行できます。
``` python
import torch
import numpy as np
from diffusers import AutoencoderKLWan, WanImageToVideoPipeline
from diffusers.utils import export_to_video, load_image
from transformers import CLIPVisionModel

# 利用可能なモデル： Wan-AI/Wan2.1-I2V-14B-480P-Diffusers, Wan-AI/Wan2.1-I2V-14B-720P-Diffusers
model_id = "Wan-AI/Wan2.1-I2V-14B-720P-Diffusers"
image_encoder = CLIPVisionModel.from_pretrained(model_id, subfolder="image_encoder", torch_dtype=torch.float32)
vae = AutoencoderKLWan.from_pretrained(model_id, subfolder="vae", torch_dtype=torch.float32)
pipe = WanImageToVideoPipeline.from_pretrained(model_id, vae=vae, image_encoder=image_encoder, torch_dtype=torch.bfloat16)
pipe.to("cuda")

image = load_image(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/astronaut.jpg"
)
max_area = 720 * 1280
aspect_ratio = image.height / image.width
mod_value = pipe.vae_scale_factor_spatial * pipe.transformer.config.patch_size[1]
height = round(np.sqrt(max_area * aspect_ratio)) // mod_value * mod_value
width = round(np.sqrt(max_area / aspect_ratio)) // mod_value * mod_value
image = image.resize((width, height))
prompt = (
    "An astronaut hatching from an egg, on the surface of the moon, the darkness and depth of space realised in "
    "the background. High quality, ultrarealistic detail and breath-taking movie-like camera shot."
)
negative_prompt = "Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, images, static, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards"

output = pipe(
    image=image,
    prompt=prompt,
    negative_prompt=negative_prompt,
    height=height, width=width,
    num_frames=81,
    guidance_scale=5.0
).frames[0]
export_to_video(output, "output.mp4", fps=16)

```
> 💡補足：この例には、プロンプト拡張と分散推論は含まれていません。プロンプト拡張と複数 GPU に対応した Diffusers 版を近日中に公開する予定です。


##### (4) ローカルで Gradio を実行する場合

```sh
cd gradio
# Gradio で 480P モデルのみを使う場合
DASH_API_KEY=your_key python i2v_14B_singleGPU.py --prompt_extend_method 'dashscope' --ckpt_dir_480p ./Wan2.1-I2V-14B-480P

# Gradio で 720P モデルのみを使う場合
DASH_API_KEY=your_key python i2v_14B_singleGPU.py --prompt_extend_method 'dashscope' --ckpt_dir_720p ./Wan2.1-I2V-14B-720P

# Gradio で 480P・720P の両モデルを使う場合
DASH_API_KEY=your_key python i2v_14B_singleGPU.py --prompt_extend_method 'dashscope' --ckpt_dir_480p ./Wan2.1-I2V-14B-480P --ckpt_dir_720p ./Wan2.1-I2V-14B-720P
```


<a id="run-first-last-frame-to-video-generation"></a>

#### 開始・終了フレームからの動画生成

開始・終了フレームからの動画生成も、プロンプト拡張を使う場合と使わない場合に分けて説明します。現在は 720P のみに対応しています。モデルの対応状況は次のとおりです。
<table>
    <thead>
        <tr>
            <th rowspan="2">タスク</th>
            <th colspan="2">解像度</th>
            <th rowspan="2">モデル</th>
        </tr>
        <tr>
            <th>480P</th>
            <th>720P</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>flf2v-14B</td>
            <td style="color: green;">❌</td>
            <td style="color: green;">✔️</td>
            <td>Wan2.1-FLF2V-14B-720P</td>
        </tr>
    </tbody>
</table>


##### (1) プロンプト拡張を使わない場合

- 単一 GPU での推論
```sh
python generate.py --task flf2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-FLF2V-14B-720P --first_frame examples/flf2v_input_first_frame.png --last_frame examples/flf2v_input_last_frame.png --prompt "CG animation style, a small blue bird takes off from the ground, flapping its wings. The bird’s feathers are delicate, with a unique pattern on its chest. The background shows a blue sky with white clouds under bright sunshine. The camera follows the bird upward, capturing its flight and the vastness of the sky from a close-up, low-angle perspective."
```

> 💡画像からの動画生成と同様に、`size` は生成動画の面積（総画素数）を指定します。アスペクト比は入力画像に合わせて決まります。


- FSDP + xDiT USP を使った複数 GPU での推論

```sh
pip install "xfuser>=0.4.1"
torchrun --nproc_per_node=8 generate.py --task flf2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-FLF2V-14B-720P --first_frame examples/flf2v_input_first_frame.png --last_frame examples/flf2v_input_last_frame.png --dit_fsdp --t5_fsdp --ulysses_size 8 --prompt "CG animation style, a small blue bird takes off from the ground, flapping its wings. The bird’s feathers are delicate, with a unique pattern on its chest. The background shows a blue sky with white clouds under bright sunshine. The camera follows the bird upward, capturing its flight and the vastness of the sky from a close-up, low-angle perspective."
```

##### (2) プロンプト拡張を使う場合


プロンプト拡張の手順は、[こちら](#2-using-prompt-extention)をご覧ください。

`Qwen/Qwen2.5-VL-7B-Instruct` によるローカルのプロンプト拡張を使う場合：
```
python generate.py --task flf2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-FLF2V-14B-720P --first_frame examples/flf2v_input_first_frame.png --last_frame examples/flf2v_input_last_frame.png --use_prompt_extend --prompt_extend_model Qwen/Qwen2.5-VL-7B-Instruct --prompt "CG animation style, a small blue bird takes off from the ground, flapping its wings. The bird’s feathers are delicate, with a unique pattern on its chest. The background shows a blue sky with white clouds under bright sunshine. The camera follows the bird upward, capturing its flight and the vastness of the sky from a close-up, low-angle perspective."
```

`dashscope` によるリモートのプロンプト拡張を使う場合：
```
DASH_API_KEY=your_key python generate.py --task flf2v-14B --size 1280*720 --ckpt_dir ./Wan2.1-FLF2V-14B-720P --first_frame examples/flf2v_input_first_frame.png --last_frame examples/flf2v_input_last_frame.png --use_prompt_extend --prompt_extend_method 'dashscope' --prompt "CG animation style, a small blue bird takes off from the ground, flapping its wings. The bird’s feathers are delicate, with a unique pattern on its chest. The background shows a blue sky with white clouds under bright sunshine. The camera follows the bird upward, capturing its flight and the vastness of the sky from a close-up, low-angle perspective."
```


##### (3) ローカルで Gradio を実行する場合

```sh
cd gradio
# Gradio で 720P モデルを使う場合
DASH_API_KEY=your_key python flf2v_14B_singleGPU.py --prompt_extend_method 'dashscope' --ckpt_dir_720p ./Wan2.1-FLF2V-14B-720P
```


<a id="run-vace"></a>

#### VACE の実行

[VACE](https://github.com/ali-vilab/VACE) は現在、2 種類のモデル（1.3B と 14B）と、主に 2 種類の解像度（480P と 720P）に対応しています。
入力は任意の解像度に対応していますが、最適な結果を得るには、動画サイズを一定の範囲内に収める必要があります。
各モデルの対応状況は次のとおりです。

<table>
    <thead>
        <tr>
            <th rowspan="2">タスク</th>
            <th colspan="2">解像度</th>
            <th rowspan="2">モデル</th>
        </tr>
        <tr>
            <th>480P(~81x480x832)</th>
            <th>720P(~81x720x1280)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>VACE</td>
            <td style="color: green; text-align: center; vertical-align: middle;">✔️</td>
            <td style="color: green; text-align: center; vertical-align: middle;">✔️</td>
            <td>Wan2.1-VACE-14B</td>
        </tr>
        <tr>
            <td>VACE</td>
            <td style="color: green; text-align: center; vertical-align: middle;">✔️</td>
            <td style="color: red; text-align: center; vertical-align: middle;">❌</td>
            <td>Wan2.1-VACE-1.3B</td>
        </tr>
    </tbody>
</table>

VACE では、テキストプロンプトに加え、必要に応じて動画、マスク、画像を入力し、動画の生成や編集を行えます。詳しい使い方は[ユーザーガイド](https://github.com/ali-vilab/VACE/blob/main/UserGuide.md)をご覧ください。
実行手順は次のとおりです。

##### (1) 前処理

用意した素材は、`src_video`、`src_mask`、`src_ref_images`、`prompt` など、VACE が認識できる入力形式に前処理する必要があります。
R2V（参照画像からの動画生成）ではこの前処理を省略できます。一方、V2V（動画からの動画編集）と MV2V（マスクを用いた動画編集）では、深度、ポーズ、マスク領域などの条件情報を持つ動画を得るために、追加の前処理が必要です。
詳しくは [vace_preproccess](https://github.com/ali-vilab/VACE/blob/main/vace/vace_preproccess.py) をご覧ください。

##### (2) CLI での推論

- 単一 GPU での推論
```sh
python generate.py --task vace-1.3B --size 832*480 --ckpt_dir ./Wan2.1-VACE-1.3B --src_ref_images examples/girl.png,examples/snake.png --prompt "在一个欢乐而充满节日气氛的场景中，穿着鲜艳红色春服的小女孩正与她的可爱卡通蛇嬉戏。她的春服上绣着金色吉祥图案，散发着喜庆的气息，脸上洋溢着灿烂的笑容。蛇身呈现出亮眼的绿色，形状圆润，宽大的眼睛让它显得既友善又幽默。小女孩欢快地用手轻轻抚摸着蛇的头部，共同享受着这温馨的时刻。周围五彩斑斓的灯笼和彩带装饰着环境，阳光透过洒在她们身上，营造出一个充满友爱与幸福的新年氛围。"
```

- FSDP + xDiT USP を使った複数 GPU での推論

```sh
torchrun --nproc_per_node=8 generate.py --task vace-14B --size 1280*720 --ckpt_dir ./Wan2.1-VACE-14B --dit_fsdp --t5_fsdp --ulysses_size 8 --src_ref_images examples/girl.png,examples/snake.png --prompt "在一个欢乐而充满节日气氛的场景中，穿着鲜艳红色春服的小女孩正与她的可爱卡通蛇嬉戏。她的春服上绣着金色吉祥图案，散发着喜庆的气息，脸上洋溢着灿烂的笑容。蛇身呈现出亮眼的绿色，形状圆润，宽大的眼睛让它显得既友善又幽默。小女孩欢快地用手轻轻抚摸着蛇的头部，共同享受着这温馨的时刻。周围五彩斑斓的灯笼和彩带装饰着环境，阳光透过洒在她们身上，营造出一个充满友爱与幸福的新年氛围。"
```

##### (3) ローカルで Gradio を実行する場合
- 単一 GPU での推論
```sh
python gradio/vace.py --ckpt_dir ./Wan2.1-VACE-1.3B
```

- FSDP + xDiT USP を使った複数 GPU での推論
```sh
python gradio/vace.py --mp --ulysses_size 8 --ckpt_dir ./Wan2.1-VACE-14B/
```

#### テキストからの画像生成

Wan2.1 は、画像と動画の両方を生成できる統合モデルです。両方のデータで学習しているため、静止画像も生成できます。画像生成のコマンドは動画生成とほぼ同じで、次のように実行します。

##### (1) プロンプト拡張を使わない場合

- 単一 GPU での推論
```sh
python generate.py --task t2i-14B --size 1024*1024 --ckpt_dir ./Wan2.1-T2V-14B  --prompt '一个朴素端庄的美人'
```

- FSDP + xDiT USP を使った複数 GPU での推論

```sh
torchrun --nproc_per_node=8 generate.py --dit_fsdp --t5_fsdp --ulysses_size 8 --base_seed 0 --frame_num 1 --task t2i-14B  --size 1024*1024 --prompt '一个朴素端庄的美人' --ckpt_dir ./Wan2.1-T2V-14B
```

##### (2) プロンプト拡張を使う場合

- 単一 GPU での推論
```sh
python generate.py --task t2i-14B --size 1024*1024 --ckpt_dir ./Wan2.1-T2V-14B  --prompt '一个朴素端庄的美人' --use_prompt_extend
```

- FSDP + xDiT USP を使った複数 GPU での推論
```sh
torchrun --nproc_per_node=8 generate.py --dit_fsdp --t5_fsdp --ulysses_size 8 --base_seed 0 --frame_num 1 --task t2i-14B  --size 1024*1024 --ckpt_dir ./Wan2.1-T2V-14B --prompt '一个朴素端庄的美人' --use_prompt_extend
```


## 人手による評価

##### (1) テキストからの動画生成の評価

人手による評価では、プロンプト拡張を行って生成した動画が、クローズドソース・オープンソース双方のモデルによる生成結果を上回りました。

<div align="center">
    <img src="assets/t2v_res.jpg" alt="" style="width: 80%;" />
</div>


##### (2) 画像からの動画生成の評価

画像からの動画生成モデルについても、大規模な人手評価を行いました。結果は下表のとおりです。**Wan2.1** が、クローズドソース・オープンソース双方のモデルを上回ることが明確に示されています。

<div align="center">
    <img src="assets/i2v_res.png" alt="" style="width: 80%;" />
</div>


## GPU ごとの計算効率

各種 GPU で **Wan2.1** の各モデルの計算効率を測定した結果を、下表に示します。数値は **合計時間（秒） / GPU メモリのピーク使用量（GB）** の形式で記載しています。


<div align="center">
    <img src="assets/comp_effic.png" alt="" style="width: 80%;" />
</div>

> この表の測定では、次の設定を使用しています。
> (1) 1.3B モデルを GPU 8 基で実行する場合は、`--ring_size 8` と `--ulysses_size 1` を設定。
> (2) 14B モデルを GPU 1 基で実行する場合は、`--offload_model True` を設定。
> (3) 1.3B モデルを RTX 4090 1 基で実行する場合は、`--offload_model True --t5_cpu` を設定。
> (4) すべての測定でプロンプト拡張は使用せず、`--use_prompt_extend` は無効。

> 💡補足：T2V-14B の方が I2V-14B より遅いのは、サンプリングのステップ数が前者では 50、後者では 40 であるためです。


-------

## Wan2.1 の概要

**Wan2.1** は、広く用いられている Diffusion Transformer を基盤に、さまざまな技術革新によって生成能力を大きく向上させています。独自の時空間変分オートエンコーダ（VAE）、規模を拡大しやすい学習戦略、大規模データセットの構築、自動評価指標などを組み合わせ、モデルの性能と汎用性を高めています。


##### (1) 3 次元変分オートエンコーダ
動画生成に特化した新しい 3 次元因果 VAE アーキテクチャ、**Wan-VAE** を提案します。複数の手法を組み合わせることで、時空間の圧縮性能を高め、メモリ使用量を削減し、時間方向の因果性を維持しています。**Wan-VAE** は、他のオープンソース VAE と比べて、性能と効率に大きな優位性があります。さらに、過去の時間情報を失うことなく、長さに制限なく 1080P 動画をエンコード・デコードできるため、動画生成タスクに特に適しています。


<div align="center">
    <img src="assets/video_vae_res.jpg" alt="" style="width: 80%;" />
</div>


##### (2) 動画拡散モデル DiT

**Wan2.1** は、広く用いられている Diffusion Transformer を基盤に、Flow Matching の枠組みで設計されています。T5 エンコーダで多言語のテキスト入力を符号化し、各 Transformer ブロックのクロスアテンションを通じてテキスト情報をモデルに組み込みます。また、Linear 層と SiLU 層を備えた MLP で入力の時間埋め込みを処理し、6 つの変調パラメータを個別に予測します。この MLP はすべての Transformer ブロックで共有され、各ブロックはそれぞれ固有のバイアスを学習します。実験では、同じパラメータ規模でも、この手法によって性能が大幅に向上することを確認しました。

<div align="center">
    <img src="assets/video_dit_arch.jpg" alt="" style="width: 80%;" />
</div>


| モデル | 隠れ次元数 | 入力次元数 | 出力次元数 | フィードフォワード層の次元数 | 周波数埋め込みの次元数 | ヘッド数 | 層数 |
|--------|-----------|-----------------|------------------|-----------------------|---------------------|-----------------|------------------|
| 1.3B   | 1536      | 16              | 16               | 8960                  | 256                 | 12              | 30               |
| 14B   | 5120       | 16              | 16               | 13824                 | 256                 | 40              | 40               |



##### データ

大量の画像・動画データから候補データセットを選別し、重複を除去しました。その過程で、基本的な特性、視覚的な品質、動きの品質に着目した 4 段階のデータクリーニングを設計しました。この堅牢なデータ処理パイプラインにより、高品質で多様な画像・動画の大規模学習データセットを容易に構築できます。

![figure1](assets/data_for_diff_stage.jpg "figure1")


##### 最先端モデルとの比較
**Wan2.1** の性能を評価するため、主要なオープンソースモデルおよびクローズドソースモデルと比較しました。独自に設計した 1,035 件のプロンプトを用い、14 の主要評価項目と 26 の詳細評価項目にわたって検証しました。各項目のスコアに、人による比較評価から得た選好に基づく重みを付けて、総合スコアを算出しています。詳細な結果は下表のとおりです。オープンソース・クローズドソース双方のモデルに対する、本モデルの優位性が示されています。

![figure1](assets/vben_vs_sota.png "figure1")


## 引用
本研究が役立った場合は、以下の文献を引用してください。

```
@article{wan2025,
      title={Wan: Open and Advanced Large-Scale Video Generative Models},
      author={Team Wan and Ang Wang and Baole Ai and Bin Wen and Chaojie Mao and Chen-Wei Xie and Di Chen and Feiwu Yu and Haiming Zhao and Jianxiao Yang and Jianyuan Zeng and Jiayu Wang and Jingfeng Zhang and Jingren Zhou and Jinkai Wang and Jixuan Chen and Kai Zhu and Kang Zhao and Keyu Yan and Lianghua Huang and Mengyang Feng and Ningyi Zhang and Pandeng Li and Pingyu Wu and Ruihang Chu and Ruili Feng and Shiwei Zhang and Siyang Sun and Tao Fang and Tianxing Wang and Tianyi Gui and Tingyu Weng and Tong Shen and Wei Lin and Wei Wang and Wei Wang and Wenmeng Zhou and Wente Wang and Wenting Shen and Wenyuan Yu and Xianzhong Shi and Xiaoming Huang and Xin Xu and Yan Kou and Yangyu Lv and Yifei Li and Yijing Liu and Yiming Wang and Yingya Zhang and Yitong Huang and Yong Li and You Wu and Yu Liu and Yulin Pan and Yun Zheng and Yuntao Hong and Yupeng Shi and Yutong Feng and Zeyinzi Jiang and Zhen Han and Zhi-Fan Wu and Ziyu Liu},
      journal = {arXiv preprint arXiv:2503.20314},
      year={2025}
}
```

## ライセンス
このリポジトリのモデルは Apache 2.0 ライセンスで提供されています。私たちは、ユーザーが生成したコンテンツに対する権利を主張しません。本ライセンスの条項を遵守する限り、生成したコンテンツを自由に利用できます。モデルの利用に関する責任は、すべてユーザーが負います。適用される法令に違反するコンテンツ、個人や集団に危害を及ぼすコンテンツ、危害を加える目的で個人情報を拡散するコンテンツ、誤情報を広めるコンテンツ、弱い立場にある人々を標的とするコンテンツを共有するために利用してはなりません。制限事項の全容とユーザーの権利に関する詳細は、[ライセンス全文](LICENSE.txt)をご覧ください。


## 謝辞

研究成果をオープンに公開してくださっている [SD3](https://huggingface.co/stabilityai/stable-diffusion-3-medium)、[Qwen](https://huggingface.co/Qwen)、[umt5-xxl](https://huggingface.co/google/umt5-xxl)、[diffusers](https://github.com/huggingface/diffusers)、[HuggingFace](https://huggingface.co) の各リポジトリの貢献者の皆さまに感謝します。



## お問い合わせ
研究チームや製品チームへのご意見・ご連絡は、[Discord](https://discord.gg/AKNgpMK4Yj) または [WeChat グループ](https://gw.alicdn.com/imgextra/i2/O1CN01tqjWFi1ByuyehkTSB_!!6000000000015-0-tps-611-1279.jpg)へお気軽にお寄せください！
