from pathlib import Path
from typing import NamedTuple

from utils import Vec2, benchmark


class Data(NamedTuple):
    lines: list[str]


@benchmark
def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_04.txt") as f:
        file = f.read().strip().splitlines()
    return Data(file)


def print_grid(grid: list[str], store: list[Vec2]):
    copy = [[x for x in y] for y in grid]
    for p in store:
        copy[p.y][p.x] = "x"

    for y in copy:
        print(" ".join(y))


def get_papers(grid: list[str] | list[list[str]]) -> list[Vec2]:
    papers_to_remove: list[Vec2] = []

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != "@":
                continue

            pos = Vec2(x, y)
            paper_count = 0
            for n in pos.neighbors_8():
                if n.x >= len(line) or 0 > n.x or n.y < 0 or n.y >= len(grid):
                    continue

                if grid[n.y][n.x] == "@":
                    paper_count += 1

            if paper_count < 4:
                papers_to_remove.append(pos)

    return papers_to_remove


@benchmark
def part_1(data: Data) -> None:
    papers = get_papers(data.lines)
    result = len(papers)

    print(f"Day 04, Part 1: {result}")


@benchmark
def part_2(data: Data) -> None:
    result = 0
    grid = [[x for x in y] for y in data.lines]

    while True:
        papers_to_remove = get_papers(grid)

        if not papers_to_remove:
            break

        result += len(papers_to_remove)
        for p in papers_to_remove:
            grid[p.y][p.x] = "."

    print(f"Day 04, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
