"""Module for 2025's day 3, part 2 of advent of code."""

from pathlib import Path

EXAMPLE = Path("example.txt")
INPUT = Path("input.txt")

NBR_COUNT = 12


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
        nbr = 0
        last_i = -1

        for cnt in range(NBR_COUNT):
            if cnt != NBR_COUNT - 1:
                d, i = max_with_i(lst[last_i+1:(-NBR_COUNT + 1 + cnt)])
            else:
                d, i = max_with_i(lst[last_i+1:])
            last_i = (last_i + 1) + i
            nbr = nbr * 10 + d

        print(nbr)

        max_nums.append(nbr)

    print(sum(max_nums))


if __name__ == "__main__":
    _main(INPUT)
