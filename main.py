#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (<= 200 characters) explaining the modern
internet to someone arriving from 1800, using only words that existed
in their time, to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "A web of thin wires joins house to house across the whole earth, "
    "so a letter sent here is read at once a thousand miles off, and "
    "more books than any library could hold stand open on a single shelf."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
