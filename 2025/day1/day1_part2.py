"""Module for 2025's day 1, part 2 of advent of code."""

from pathlib import Path

FILE_PATH = Path("input.txt")


def _main() -> None:
    # Read file
    text = FILE_PATH.read_text(encoding="utf-8")

    # Get instructions
    lines = text.splitlines()
    instructions = [(line[0], int(line[1:])) for line in lines]

    # Go through instructions
    pos = 50
    nbr_at_zero = 0

    for direction_str, nbr in instructions:
        direction = 1 if direction_str == "R" else -1

        # Go through each step one by one
        # Not efficient but works
        for _ in range(nbr):
            pos += direction
            pos %= 100

            if pos == 0:
                nbr_at_zero += 1

    print(nbr_at_zero)


if __name__ == "__main__":
    _main()
