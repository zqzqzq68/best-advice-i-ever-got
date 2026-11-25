#!/usr/bin/env python3
"""Write one sentence of advice to /output/entry.txt and print it.

The sentence is the best advice the writer ever received, told in a
single sentence of 147 characters. The program is deterministic: it
writes the same text on every run, uses only the standard library,
and touches no network, no clock and no randomness.
"""

import os

SENTENCE = "My grandmother said to wash the last pan before bed, because a clean kitchen at night is a small kindness to the person you will be in the morning."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
