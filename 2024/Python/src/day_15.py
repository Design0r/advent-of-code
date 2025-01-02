from copy import deepcopy
from pathlib import Path
from typing import NamedTuple

from utils import Vec2, benchmark

Grid = list[list[str]]


class Data(NamedTuple):
    grid: Grid
    instructions: str
    robot: Vec2


DIRS = {"<": Vec2(-1, 0), "^": Vec2(0, -1), ">": Vec2(1, 0), "v": Vec2(0, 1)}


@benchmark
def parse() -> Data:
    with open(Path(__file__).parent.parent / "samples/day_15.txt") as f:
        grid, instructions = f.read().strip().split("\n\n")

    grid = [[x for x in y] for y in grid.splitlines()]
    robot = [
        Vec2(x, y)
        for y, row in enumerate(grid)
        for x, col in enumerate(row)
        if col == "@"
    ][0]

    return Data(grid, "".join(instructions.splitlines()), robot)


def move_boxes(grid: list[list[str]], pos: Vec2, dir: Vec2) -> Vec2:
    num_boxes = 0
    next_pos = pos
    robot_pos = pos
    move = True
    steps = 0
    while True:
        next_pos += dir
        if (
            next_pos.y < 0
            or next_pos.y >= len(grid)
            or next_pos.x < 0
            or next_pos.x >= len(grid[0])
        ):
            break
        next_val = grid[next_pos.y][next_pos.x]
        if next_val == "#":
            break

        if next_val in ("O"):
            num_boxes += 1

        if move:
            robot_pos = next_pos
            move = False

        steps += 1

        if next_val == ".":
            break

    if steps == num_boxes:
        robot_pos = pos

    fill_pos = robot_pos
    for _ in range(num_boxes):
        fill_pos += dir
        grid[fill_pos.y][fill_pos.x] = "O"

    grid[pos.y][pos.x] = "."
    grid[robot_pos.y][robot_pos.x] = "@"

    return robot_pos


def move_big_boxes(grid: list[list[str]], pos: Vec2, dir: Vec2) -> Vec2:
    num_boxes = 0
    next_pos = pos
    robot_pos = pos
    move = True
    steps = 0
    boxes_to_move: list[Vec2] = []
    while True:
        next_pos += dir
        if (
            next_pos.y < 0
            or next_pos.y >= len(grid)
            or next_pos.x < 0
            or next_pos.x >= len(grid[0])
        ):
            break
        next_val = grid[next_pos.y][next_pos.x]
        if next_val == "#":
            break

        if dir.x != 0:
            if next_val == "[" or next_val == "]":
                boxes_to_move.append(next_pos)
        else:
            if next_val == "[":
                boxes_to_move.append(next_pos)
                boxes_to_move.append(next_pos + DIRS[">"])
            elif next_val == "]":
                boxes_to_move.append(next_pos)
                boxes_to_move.append(next_pos + DIRS["<"])

        if move:
            robot_pos = next_pos
            move = False

        steps += 1

        if next_val == ".":
            break

    if steps == num_boxes:
        robot_pos = pos

    fill_pos = robot_pos
    for box in boxes_to_move:
        fill_pos += dir
        grid[fill_pos.y][fill_pos.x] = "O"

    grid[pos.y][pos.x] = "."
    grid[robot_pos.y][robot_pos.x] = "@"

    return robot_pos


def print_grid(grid: list[list[str]]):
    for row in grid:
        print("".join(row))

    print(f"{80*'='}")


def calc_gps(grid: Grid) -> int:
    return sum(
        (100 * y) + x
        for y, row in enumerate(grid)
        for x, col in enumerate(row)
        if col == "O"
    )


def parse_wide_grid(grid: Grid) -> Grid:
    new_grid: Grid = []
    for row in grid:
        new_row: list[str] = []
        for col in row:
            if col == "#":
                new_row.extend(("#", "#"))
            elif col == "O":
                new_row.extend(("[", "]"))
            elif col == ".":
                new_row.extend((".", "."))
            elif col == "@":
                new_row.extend(("@", "."))
        new_grid.append(new_row)

    return new_grid


@benchmark
def part_1(data: Data) -> None:
    grid = deepcopy(data.grid)
    curr_pos = data.robot
    for inst in data.instructions:
        curr_pos = move_boxes(grid, curr_pos, DIRS[inst])
    result = calc_gps(grid)

    print(f"Day 15, Part 1: {result}")


@benchmark
def part_2(data: Data) -> None:
    result = 0
    grid = parse_wide_grid(data.grid)
    print_grid(grid)
    print(f"Day 15, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
