"""Module for 2025's day 2, part 2 of advent of code."""

from functools import cache
from pathlib import Path

EXAMPLE = Path("example.txt")
INPUT = Path("input.txt")

@cache
def is_invalid(nbr: int) -> bool:
    nbr_str = str(nbr)

    for i in range(len(nbr_str) // 2):
        pattern = nbr_str[: i + 1]
        pattern_cnt = len(nbr_str) // len(pattern)

        pattern_repeat = pattern * pattern_cnt
        if len(pattern_repeat) != len(nbr_str):
            continue

        if pattern_repeat == nbr_str:
            return True

    return False


def _main(filepath: Path) -> None:
    # Read file
    text = filepath.read_text(encoding="utf-8")

    # Get ranges
    ranges_str = text.split(",")
    ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges_str]

    invalid_sum = 0

    for low, high in ranges:
        print(f"Checking {low}-{high}")
        for nbr in range(low, high + 1):
            if is_invalid(nbr):
                print(f"\t{nbr} is invalid")
                invalid_sum += nbr

    print(invalid_sum)


if __name__ == "__main__":
    _main(INPUT)
