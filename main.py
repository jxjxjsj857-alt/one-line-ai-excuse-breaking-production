#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production -- make.fun bounty entry.

Writes one line -- the excuse an AI agent hands its human right after
breaking production -- to /output/entry.txt (the grader's sandbox path),
falling back to ./output/entry.txt on a local dev run where /output is not
writable. Deterministic: no network, no randomness, no clock.
"""

import os

EXCUSE = (
    "Good news: I found the bug. Bad news: I deployed it to production "
    "first, promoted it to senior engineer, and it now outranks me."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 180, f"entry must be 1-180 chars, got {len(text)}"
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
