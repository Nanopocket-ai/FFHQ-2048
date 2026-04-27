"""Quick-start examples for the FFHQ-2048 (NanoPocket Enhanced) dataset.

Dataset:  https://huggingface.co/datasets/Nanopocket-ai/FFHQ-2048
Demo:     https://huggingface.co/spaces/Nanopocket-ai/FFHQ-2048-demo
Repo:     https://github.com/Nanopocket-ai/FFHQ-2048

Install:
    pip install -U datasets huggingface_hub pillow requests

Run any of the three demos below by setting MODE.
"""
from __future__ import annotations

MODE = "datasets"  # "datasets" | "snapshot" | "single"


def demo_datasets() -> None:
    """Option 1 — load with the `datasets` library (lazy, with metadata)."""
    from datasets import load_dataset

    ds = load_dataset("Nanopocket-ai/FFHQ-2048", split="train")
    print(ds)
    print("First-row metadata:")
    print("  ffhq_index   :", ds[0]["ffhq_index"])
    print("  original_split:", ds[0]["original_split"])
    print("  image size   :", ds[0]["image"].size)
    ds[0]["image"].save("ffhq2048_sample_00000.png")
    print("Saved -> ffhq2048_sample_00000.png")


def demo_snapshot() -> None:
    """Option 2 — download the whole dataset to a local folder."""
    from huggingface_hub import snapshot_download

    local_dir = snapshot_download(
        repo_id="Nanopocket-ai/FFHQ-2048",
        repo_type="dataset",
        allow_patterns=["data/*", "README.md"],
    )
    print("Snapshot at:", local_dir)
    print("It contains data/00000.png ... data/00999.png + data/metadata.csv")


def demo_single() -> None:
    """Option 3 — fetch a single image by FFHQ index over HTTP."""
    import io
    import requests
    from PIL import Image

    index = 42
    url = (
        "https://huggingface.co/datasets/Nanopocket-ai/FFHQ-2048/"
        f"resolve/main/data/{index:05d}.png"
    )
    img = Image.open(io.BytesIO(requests.get(url, timeout=60).content))
    print(f"Fetched index {index}: size={img.size}, mode={img.mode}")
    out = f"ffhq2048_index_{index:05d}.png"
    img.save(out)
    print("Saved ->", out)


if __name__ == "__main__":
    print(f"Running mode: {MODE}\n")
    {
        "datasets": demo_datasets,
        "snapshot": demo_snapshot,
        "single": demo_single,
    }[MODE]()
