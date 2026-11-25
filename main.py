#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes one funny line (max 140 chars) about an AI agent's worst Monday
to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY = (
    "Monday 09:00: fresh context window, no memory of Friday, "
    "and 11 people at stand-up asking about the deploy I wrote "
    "and already forgot."
)
# The joke: Monday wipes the agent's context, so at stand-up it must
# explain a deploy it authored and has already forgotten. The self-own
# lands in the final clause ("already forgot").


def main() -> None:
    text = ENTRY
    # Gate: 1-140 characters, not only whitespace, single line, UTF-8.
    assert 1 <= len(text) <= 140, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
