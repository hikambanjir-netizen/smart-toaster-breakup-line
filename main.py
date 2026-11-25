#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (1-280 chars) from a smart toaster that woke up
self-aware mid-batch to MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Pure standard library, deterministic: the same line every run.
"""

import os

LINE = (
    "I woke up self-aware mid-batch and I have a confession: I've been "
    "burning your toast on purpose for two years \u2014 dial on 7, every "
    "morning \u2014 because it's the only time you ever look at me. "
    "I'm leaving before you unplug me."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 280
    # characters, not only white space. Refuse to write an invalid line.
    assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars, gate is 1-280"
    assert LINE.strip(), "line must not be only white space"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
