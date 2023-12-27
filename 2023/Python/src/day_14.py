from pathlib import Path
from utils import timeit

file = open(Path(__file__).parent.parent / "inputs/day_14.txt").read().splitlines()

rock = "O"
empty = "."
collison = {"#", rock}


def move(grid, y, x):
    next_y = y - 1
    if 0 <= next_y and grid[next_y][x] not in collison:
        grid[next_y][x], grid[y][x] = rock, empty
        move(grid, next_y, x)
    return grid


@timeit
def part_1():
    grid = [list(line) for line in file]

    for row_idx, line in enumerate(grid):
        if row_idx == 0:
            continue
        for col_idx, obj in enumerate(line):
            if obj != "O":
                continue
            move(grid, row_idx, col_idx)

    result = sum(
        row_idx
        for row_idx, line in enumerate(reversed(grid), 1)
        for obj in line
        if obj == rock
    )

    print("Day 14, Part 1:", result)


def rotate_grid(grid: list[list[str]]):
    list_of_tuples = zip(*grid)
    return [list(reversed(elem)) for elem in list_of_tuples]


def print_grid(grid):
    print("#" * 20)
    for l in grid:
        print(" ".join(l))


def to_hashable(grid: list[list[str]]) -> tuple[str]:
    return tuple("".join(line) for line in grid)


@timeit
def part_2():
    grid = [list(line) for line in file]
    temp_grid = to_hashable(grid)
    seen = {temp_grid}
    seen_list = [temp_grid]
    CYCLES = 1_000_000_000

    for cycle in range(CYCLES):
        for _ in range(4):
            for row_idx, line in enumerate(grid):
                for col_idx, obj in enumerate(line):
                    if obj != "O":
                        continue
                    move(grid, row_idx, col_idx)
            grid = rotate_grid(grid)

        temp_grid = to_hashable(grid)
        if temp_grid in seen:
            break

        seen.add(temp_grid)
        seen_list.append(temp_grid)

    first = seen_list.index(temp_grid)
    index = (CYCLES - first) % (cycle + 1 - first) + first
    final_grid = seen_list[index]

    result = sum(
        row_idx
        for row_idx, line in enumerate(reversed(final_grid), 1)
        for obj in line
        if obj == rock
    )

    print("Day 14, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
