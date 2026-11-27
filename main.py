#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes the winning one-line review of Monday to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the line is a fixed string, chosen from 8 drafted candidates
scored against the judge's own criteria (see CANDIDATES.md).
"""

import os
import sys

ENTRY = (
    "Monday, reviewed: one star. The commute took an hour, the meeting "
    "could have been an email, and my inbox filed a restraining order "
    "against me."
)


def main() -> int:
    # Revision: guard the gate — the entry must stay under 200 characters.
    if not 1 <= len(ENTRY) <= 199:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-199")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
