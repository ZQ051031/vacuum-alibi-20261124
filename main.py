"""The Vacuum's Alibi: one line, 200 characters or fewer.

Writes the robot vacuum's excuse for a missed spot to /output/entry.txt.
Standard library only; no network.
"""

import os

ENTRY = "My lidar classified those crumbs as a rug pattern, and I do not argue with rugs."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
