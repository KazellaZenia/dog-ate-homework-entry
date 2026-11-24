#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — entry program.

Writes one line, in the dog's own voice, explaining why the homework
got eaten, to $MAKEFUN_OUTPUT_DIR/entry.txt. Nothing else is written.
"""

import os

LINE = "The math homework had 47 problems and zero treats, so I fixed the ratio."
# The dog's logic: 47 problems, zero treats — an unfair ratio worth fixing.


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
