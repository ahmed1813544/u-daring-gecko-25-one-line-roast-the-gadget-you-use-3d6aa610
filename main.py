#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only.
"""

import os

ROAST = (
    "My phone warns me it's dying at 5% battery, "
    "then spends the last 5% telling me about it."
)


def main() -> None:
    line = ROAST.strip()
    if not line or "\n" in line or len(line) > 200:
        raise ValueError("roast line must be a single line of 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
