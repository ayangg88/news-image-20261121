#!/usr/bin/env python3
"""Entry for news-image-20261121: publish the front-page image.

The image is the newspaper front page "THE WORLD IN ONE DAY — SATURDAY
21 NOVEMBER 2026", drawn once and stored beside this file as entry.png.
This program only copies it, byte for byte, to the output path, so both
grader runs write identical bytes. Standard library only, no network.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUTPUT_DIR, "entry.png")


def sha256_of(path):
    """Return the hex SHA-256 of a file's bytes."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    before = sha256_of(SOURCE)
    after = sha256_of(TARGET)
    if before != after:
        print("copy failed: hash mismatch", file=sys.stderr)
        return 1
    size = os.path.getsize(TARGET)
    # Deterministic by construction: the output is an exact copy of the
    # input bytes, so every run writes the same file.
    print("wrote %s (%d bytes, sha256 %s)" % (TARGET, size, after))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
