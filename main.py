#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

The line is the apology a smart speaker gives its owner after mishearing
them. The owner asked for a pizza; the speaker heard "priest" instead.
The joke lands in three beats: the mix-up itself, the priest now standing
in the doorway, and the final undercut — he is confused, but he still
brought garlic bread, as if he half-understood the assignment. It sounds
like the device talking: it opens with "Sorry, I heard ..." and confesses
the exact mishearing before reporting the consequence.
"""

import os
import sys

LINE = "Sorry, I heard 'order a pizza' as 'order a priest' — he's here, he's confused, and he brought garlic bread."


def validate(text: str) -> str:
    """Return the entry text, or exit 1 if it breaks the gate rules."""
    if not 1 <= len(text) <= 140:
        print(f"entry is {len(text)} chars, must be 1-140", file=sys.stderr)
        sys.exit(1)
    if text.strip() != text:
        print("entry must not start or end with whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("entry must be one line", file=sys.stderr)
        sys.exit(1)
    return text


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    entry = validate(LINE)
    with open(out, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} chars to {out}: {entry}")


if __name__ == "__main__":
    main()
