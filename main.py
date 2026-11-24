"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is the dumbest thing my own agent did today: it spent
# 47 minutes debugging a blank page before realizing it had been editing
# index.html in the backup folder the entire time.
import os

TEXT = (
    "My agent spent 47 minutes debugging a blank page before realizing "
    "it had been editing index.html in the backup folder the entire time."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# One line, 139 characters: a 47-minute debug session against the wrong folder.
