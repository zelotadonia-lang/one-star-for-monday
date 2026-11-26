#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday, written as if
Monday were a restaurant, for the make.fun bounty
"u-clever-harbor-75-one-star-for-monday-9ead4a61".

The entry text is a single fixed sentence, reproduced exactly:

    The menu just says Monday. No prices. The waiter says you pay
    with your weekend.

The program writes that text verbatim to /output/entry.txt, with no
trailing newline. It is fully deterministic: no input, no randomness,
no clock, no network access, no environment dependence.
"""

import os

# The entry text, kept verbatim: 80 characters, 15 words. Any change
# here changes the submission, so this string is never edited casually.
ENTRY = "The menu just says Monday. No prices. The waiter says you pay with your weekend."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry text to the output path, creating it if needed."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
