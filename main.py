#!/usr/bin/env python3
"""One Line, One Laugh — writes a single original one-liner to /output/entry.txt.

Deterministic, stdlib-only, no network. The line is the whole entry.
One file, one line: the setup stays short so the punchline carries the laugh.
"""

import os

LINE = "My plants died of neglect, so I bought plastic ones \u2014 now even the fake ones look disappointed in me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
