from pathlib import Path
from typing import Generator
import sys
from utils import timeit, Vec2, StrGrid2D

sys.setrecursionlimit(1_000_000)

file = open(Path(__file__).parent.parent / "inputs/day_16.txt").read().splitlines()
grid = [list(line) for line in file]
DirPos = set[tuple[Vec2, Vec2]]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def print_grid(grid: StrGrid2D):
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


def move(grid: StrGrid2D, pos: Vec2, dir: Vec2, seen: DirPos | None = None):
    py, px = pos
    dy, dx = dir
    if not seen:
        seen = set()
        seen.add((dir, pos))
        for new_dir in get_new_dirs(grid[py][px], dir):
            move(grid, pos, new_dir, seen=seen)
        return seen

    new_pos = (py + dy, px + dx)
    ny, nx = new_pos
    if ny < 0 or ny > len(grid) - 1:
        return seen
    elif nx < 0 or nx > len(grid[0]) - 1:
        return seen
    new_symbol = grid[ny][nx]

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
    seen = move(grid, (0, 0), directions["right"])
    print("Day 16, Part 1:", count_seen(seen))


@timeit
def part_2():
    result = 0
    # top->down
    for i, _ in enumerate(grid[0]):
        seen = move(grid, (0, i), directions["down"])
        result = max(result, count_seen(seen))
    # down->top
    for i, _ in enumerate(grid[-1]):
        seen = move(grid, (0, i), directions["up"])
        result = max(result, count_seen(seen))

    rotate = tuple(zip(*grid))

    # left->right
    for i, _ in enumerate(rotate[0]):
        seen = move(grid, (i, 0), directions["right"])
        result = max(result, count_seen(seen))

    # right->left
    for i, _ in enumerate(rotate[1]):
        seen = move(grid, (i, len(grid[0]) - 1), directions["left"])
        result = max(result, count_seen(seen))

    print("Day 16, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
