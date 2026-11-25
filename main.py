#!/usr/bin/env python3
"""Write the single-line entry to /output/entry.txt."""

import os

ENTRY = (
    "After six years of night shifts and bus-seat studying, "
    "he signed the last page of his thesis on the depot bench "
    "where he'd first failed the exam."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, len(ENTRY)
    assert "\n" not in ENTRY and "\r" not in ENTRY
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
