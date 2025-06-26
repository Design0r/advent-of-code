from pathlib import Path
from typing import NamedTuple


class Data(NamedTuple):
    lines: list[str]


def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_04.txt") as f:
        file = f.read().strip().splitlines()
    return Data(file)


def part_1(data: Data) -> None:
    result = 0
    print(f"Day 04, Part 1: {result}")


def part_2(data: Data) -> None:
    result = 0
    print(f"Day 04, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
