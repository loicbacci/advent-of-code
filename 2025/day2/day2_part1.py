"""Module for 2025's day 2, part 1 of advent of code."""

from pathlib import Path

EXAMPLE = Path("example.txt")
INPUT = Path("input.txt")


def is_invalid(nbr: int) -> bool:
    nbr_str = str(nbr)

    # If odd length, not a pattern
    if len(nbr_str) % 2 == 1:
        return False

    # Check if half is repeatable
    half_len = len(nbr_str) // 2
    pattern = nbr_str[:half_len]

    return pattern * 2 == nbr_str

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
