from pathlib import Path
from typing import NamedTuple

type Point = tuple[int, int]
type Grid = dict[Point, str]
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1))


class Data(NamedTuple):
    file: list[str]
    x_pos: list[Point]
    a_pos: list[Point]
    grid: Grid


def parse() -> Data:
    file = (
        (Path(__file__).parent.parent / "inputs/day_04.txt")
        .read_text()
        .strip()
        .splitlines()
    )
    x_pos: list[Point] = []
    a_pos: list[Point] = []
    grid: Grid = {}

    for row, line in enumerate(file):
        for col, char in enumerate(line):
            grid[(col, row)] = char
            if char == "X":
                x_pos.append((col, row))
            elif char == "A":
                a_pos.append((col, row))

    return Data(file, x_pos, a_pos, grid)


def get_word(grid: Grid, start: Point, dir: Point, count: int) -> str:
    word: list[str] = []
    for i in range(count):
        grid_idx = (start[0] + dir[0] * i, start[1] + dir[1] * i)
        if grid_idx in grid:
            word.append(grid[grid_idx])

    return "".join(word)


def check_mas_x(grid: Grid, start: Point) -> bool:
    top_left = (start[0] - 1, start[1] - 1)
    word = get_word(grid, top_left, dir=(1, 1), count=3)
    if word != "MAS" and word != "SAM":
        return False

    bottom_left = (start[0] - 1, start[1] + 1)
    word = get_word(grid, bottom_left, dir=(1, -1), count=3)
    if word != "MAS" and word != "SAM":
        return False

    return True


def part_1(data: Data) -> None:
    result = 0

    for pos in data.x_pos:
        for dir in DIRECTIONS:
            if get_word(data.grid, pos, dir, len("XMAS")) == "XMAS":
                result += 1

    print(f"Day 0, Part 1: {result}")


def part_2(data: Data) -> None:
    result = sum([1 for pos in data.a_pos if check_mas_x(data.grid, pos)])
    print(f"Day 0, Part 2: {result}")


def main():
    data = parse()
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
