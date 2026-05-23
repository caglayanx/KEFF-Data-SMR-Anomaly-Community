#!/usr/bin/env python3
"""Download the KEFF Data PWR-SMR-2026-01 Community Edition dataset."""

from __future__ import annotations

import argparse
from pathlib import Path

from huggingface_hub import snapshot_download


DATASET_ID = "keffdata/pwr-smr-2026-01-community"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download the KEFF Data PWR-SMR-2026-01 dataset from Hugging Face."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/pwr-smr-2026-01-community"),
        help="Local directory for the downloaded dataset snapshot.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_dir = args.output_dir.expanduser().resolve()

    snapshot_path = snapshot_download(
        repo_id=DATASET_ID,
        repo_type="dataset",
        local_dir=target_dir,
        local_dir_use_symlinks=False,
    )

    print(f"Dataset downloaded to: {snapshot_path}")


if __name__ == "__main__":
    main()
