#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy to /output/entry.txt.
Standard library only; deterministic output.
"""

import os

LINE = (
    "The server ran out of memory while saving, so your work is gone. "
    "Not 'temporarily unavailable' -- gone. Refreshing won't bring it back."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text on one
# line. Fail loudly here rather than shipping an invalid entry.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
assert "\n" not in LINE, "line must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
