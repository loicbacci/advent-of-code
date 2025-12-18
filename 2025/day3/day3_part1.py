"""Module for 2025's day 3, part 1 of advent of code."""

from pathlib import Path

EXAMPLE = Path("example.txt")
INPUT = Path("input.txt")


def max_with_i(lst: list[int]) -> tuple[int, int]:
    max_val = lst[0]
    max_i = 0

    for i, val in enumerate(lst):
        if val > max_val:
            max_val = val
            max_i = i

    return max_val, max_i


def _main(filepath: Path) -> None:
    # Read file
    text = filepath.read_text(encoding="utf-8")

    # Get lists
    lines = text.splitlines()
    int_lists = [[int(c) for c in line] for line in lines]

    max_nums = []

    for lst in int_lists:
        # Find first digit
        d1, i1 = max_with_i(lst[:-1])

        # Find second digit
        d2, i2 = max_with_i(lst[i1+1:])
        i2 += i1+1

        nbr = d1 * 10 + d2
        print(f"{nbr} ({i1}, {i2})")

        max_nums.append(nbr)

    print(sum(max_nums))


if __name__ == "__main__":
    _main(INPUT)
