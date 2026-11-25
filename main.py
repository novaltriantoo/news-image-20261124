#!/usr/bin/env python3
"""news-image-20261124 entry program.

Copies the front-page image entry.png (sitting next to this script, or
falling back to entry.png in the current working directory) to
/output/entry.png, then verifies the written bytes are identical.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, SOURCE_NAME)


def find_source() -> str:
    """Return the path to entry.png, preferring the file beside main.py."""
    beside_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), SOURCE_NAME)
    if os.path.isfile(beside_script):
        return beside_script
    in_cwd = os.path.join(os.getcwd(), SOURCE_NAME)
    if os.path.isfile(in_cwd):
        return in_cwd
    raise SystemExit("entry.png not found next to main.py or in the current directory")


def main() -> None:
    source = find_source()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(source, OUTPUT_PATH)

    # Verify the copy byte-for-byte against the source image, so a
    # truncated or corrupted write is caught instead of silently shipped.
    with open(source, "rb") as src, open(OUTPUT_PATH, "rb") as dst:
        if src.read() != dst.read():
            raise SystemExit("entry.png verification failed: /output/entry.png differs from entry.png")
    print("Wrote /output/entry.png")


if __name__ == "__main__":
    main()
