"""Module for 2025's day 4, part 1 of advent of code."""

from pathlib import Path

EXAMPLE = Path("example.txt")
INPUT = Path("input.txt")


def is_paper(grid: list[str], x: int, y: int) -> bool:
    return grid[y][x] == "@"


def remove_paper(grid: list[str], x: int, y: int) -> list[str]:
    line = grid[y]
    new_line = line[:x] + "." + line[x+1:]
    assert len(line) == len(new_line)

    new_grid = grid[:y]
    new_grid.append(new_line)
    new_grid.extend(grid[y+1:])
    assert len(grid) == len(new_grid)

    assert not is_paper(new_grid, x, y)

    return new_grid

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
    removed_papers = True

    while removed_papers:
        removed_papers = False

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if not is_paper(grid, x, y):
                    continue

                if cnt_neighbors_paper(grid, x, y) < 4:
                    cnt += 1
                    removed_papers = True
                    grid = remove_paper(grid, x, y)

    print(cnt)


if __name__ == "__main__":
    _main(INPUT)
