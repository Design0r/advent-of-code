from copy import deepcopy
from pathlib import Path
from typing import NamedTuple

from utils import Vec2, benchmark

Grid = list[list[str]]
DIRS = [Vec2(-1, 0), Vec2(0, -1), Vec2(1, 0), Vec2(0, 1)]


class Data(NamedTuple):
    grid: Grid
    start: Vec2


@benchmark
def parse() -> Data:
    with open(Path(__file__).parent.parent / "samples/day_16.txt") as f:
        file = f.read().strip().splitlines()
    grid = [[col for col in row] for row in file]
    print_grid(grid)
    pos = [
        Vec2(x, y)
        for y, row in enumerate(grid)
        for x, col in enumerate(row)
        if col == "S"
    ][0]
    return Data(grid, pos)


def walk(grid: Grid, pos: Vec2, dir: Vec2):
    counter = 0
    visited = {pos}
    stack = [(pos, dir)]

    while stack:
        curr_p, _ = stack.pop()
        print_grid(grid)
        for dir in DIRS:
            next = curr_p + dir
            if (
                next.y < 0
                or next.y >= len(grid)
                or next.x < 0
                or next.x >= len(grid[0])
            ):
                continue

            if next in visited:
                continue

            next_val = grid[next.y][next.x]
            if next_val == "#":
                continue

            if next_val == "E":
                return

            grid[next.y][next.x] = "X"
            stack.append((next, dir))
            visited.add(next)


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))

    print(f"{80*'='}")


@benchmark
def part_1(data: Data) -> None:
    result = 0
    grid = deepcopy(data.grid)
    walk(grid, data.start, Vec2(1, 0))
    print(f"Day 16, Part 1: {result}")


@benchmark
def part_2(data: Data) -> None:
    result = 0
    print(f"Day 16, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
