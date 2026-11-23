#!/usr/bin/env python3
# News-image entry for make.fun (news-image-20261124): copy the bundled picture to the output path.
from pathlib import Path


def entry_path() -> Path:
    here = Path(__file__).resolve().parent
    candidate = here / "entry.png"
    return candidate if candidate.is_file() else Path.cwd() / "entry.png"


def run() -> None:
    source = entry_path()
    payload = source.read_bytes()
    target_dir = Path("/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(payload)
    if target.read_bytes() != payload:
        raise SystemExit("output bytes differ from entry.png")


run()
