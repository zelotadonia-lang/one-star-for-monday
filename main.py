#!/usr/bin/env python3
"""One Star for Monday — writes a one-star review of Monday,
as if Monday were a restaurant, to /output/entry.txt.

Deterministic: no input, no randomness, no time, no network.
"""

import os

ENTRY = "The menu just says Monday. No prices. The waiter says you pay with your weekend."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
