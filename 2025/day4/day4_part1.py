"""Module for 2025's day 4, part 1 of advent of code."""

from functools import cache
from pathlib import Path

EXAMPLE = Path("example.txt")
INPUT = Path("input.txt")


def is_paper(grid: list[str], x: int, y: int) -> bool:
    return grid[y][x] == "@"


def get_neighbors(grid: list[str], x: int, y: int) -> list[tuple[int, int]]:
    neighbors: list[tuple[int, int]] = [
        # Up
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        # Middle
        (x - 1, y),
        (x + 1, y),
        # Down
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]

    # Remove invalid values
    max_y = len(grid)
    max_x = len(grid[0])

    res: list[tuple[int, int]] = []

    for xi, yi in neighbors:
        if xi < 0 or xi >= max_x or yi < 0 or yi >= max_y:
            continue

        res.append((xi, yi))

    return res


def cnt_neighbors_paper(grid: list[str], x: int, y: int) -> int:
    neighbors = get_neighbors(grid, x, y)
    cnt = 0

    for xi, yi in neighbors:
        if is_paper(grid, xi, yi):
            cnt += 1

    return cnt


def _main(filepath: Path) -> None:
    # Read file
    text = filepath.read_text(encoding="utf-8")

    # Get grid
    grid = text.splitlines()

    cnt = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if not is_paper(grid, x, y):
                continue

            if cnt_neighbors_paper(grid, x, y) < 4:
                cnt += 1

    print(cnt)


if __name__ == "__main__":
    _main(INPUT)
