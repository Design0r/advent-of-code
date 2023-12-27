from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
from typing import Generator
import sys
from time import perf_counter

sys.setrecursionlimit(1_000_000_000)

file = open(Path(__file__).parent.parent / "inputs/day_16.txt").read().splitlines()
grid = [list(line) for line in file]


def timeit(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        stop = perf_counter()
        print(f"finished {func.__qualname__} in {stop-start:.3f}s")

    return wrapper


@dataclass(frozen=True, slots=True)
class Vec2:
    y: int
    x: int

    def __add__(self, __obj: Vec2):
        return Vec2(self.y + __obj.y, self.x + __obj.x)

    def __eq__(self, __obj: Vec2):
        return self.y == __obj.y and self.x == __obj.x


directions = {
    "up": Vec2(-1, 0),
    "down": Vec2(1, 0),
    "left": Vec2(0, -1),
    "right": Vec2(0, 1),
}


def print_grid(grid: list[list[str]]):
    print("=" * 20)
    for line in grid:
        print(" ".join((str(i) for i in line)))


def get_new_dirs(symbol: str, curr_dir: Vec2) -> Generator[Vec2, None, None]:
    if symbol == ".":
        yield curr_dir
    elif symbol == "/":
        if curr_dir == directions["right"]:
            yield directions["up"]
        elif curr_dir == directions["up"]:
            yield directions["right"]
        elif curr_dir == directions["down"]:
            yield directions["left"]
        else:
            yield directions["down"]

    elif symbol == "\\":
        if curr_dir == directions["right"]:
            yield directions["down"]
        elif curr_dir == directions["up"]:
            yield directions["left"]
        elif curr_dir == directions["down"]:
            yield directions["right"]
        else:
            yield directions["up"]

    elif symbol == "|":
        if curr_dir == directions["up"] or curr_dir == directions["down"]:
            yield curr_dir
        else:
            yield directions["up"]
            yield directions["down"]

    elif symbol == "-":
        if curr_dir == directions["left"] or curr_dir == directions["right"]:
            yield curr_dir
        else:
            yield directions["left"]
            yield directions["right"]


def move(grid: list[list[str]], pos: Vec2, dir: Vec2, seen=None):
    if not seen:
        seen = set()
        seen.add((dir, pos))
        for new_dir in get_new_dirs(grid[pos.y][pos.x], dir):
            move(grid, pos, new_dir, seen=seen)
        return seen

    new_pos = pos + dir
    if new_pos.y < 0 or new_pos.y > len(grid) - 1:
        return seen
    elif new_pos.x < 0 or new_pos.x > len(grid[0]) - 1:
        return seen
    new_symbol = grid[new_pos.y][new_pos.x]

    for new_dir in get_new_dirs(new_symbol, dir):
        t = (new_dir, new_pos)
        if t in seen:
            continue
        seen.add(t)
        move(grid, new_pos, new_dir, seen=seen)

    return seen


def count_seen(seen: set[tuple[Vec2, Vec2]]):
    return len({j for _, j in seen})


@timeit
def part_1():
    seen = move(grid, Vec2(0, 0), directions["right"])
    print("Day 16, Part 1:", count_seen(seen))


@timeit
def part_2():
    result = 0
    # top->down
    for i, _ in enumerate(grid[0]):
        seen = move(grid, Vec2(0, i), directions["down"])
        result = max(result, count_seen(seen))
    # down->top
    for i, _ in enumerate(grid[-1]):
        seen = move(grid, Vec2(0, i), directions["up"])
        result = max(result, count_seen(seen))

    left = (x for _, y in enumerate(grid) for ix, x in enumerate(y) if ix == 0)
    right = (
        x for _, y in enumerate(grid) for ix, x in enumerate(y) if ix == len(grid) - 1
    )
    # left->right
    for i, _ in enumerate(left):
        seen = move(grid, Vec2(i, 0), directions["right"])
        result = max(result, count_seen(seen))

    # right->left
    for i, _ in enumerate(right):
        seen = move(grid, Vec2(i, len(grid[0]) - 1), directions["left"])
        result = max(result, count_seen(seen))

    print("Day 16, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
