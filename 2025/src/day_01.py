from pathlib import Path
from typing import NamedTuple

from utils import benchmark


class Data(NamedTuple):
    lines: list[str]


@benchmark
def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_01.txt") as f:
        file = f.read().strip().splitlines()
    return Data(file)


@benchmark
def part_1(data: Data) -> None:
    result = 0
    curr_pos = 50

    for line in data.lines:
        sign = 1 if line[0] == "R" else -1
        num = int(line[1:])

        curr_pos = (curr_pos + (sign * num)) % 100
        if curr_pos == 0:
            result += 1

    print(f"Day 01, Part 1: {result}")


@benchmark
def part_2(data: Data) -> None:
    result = 0
    curr_pos = 50

    for line in data.lines:
        sign = 1 if line[0] == "R" else -1
        num = int(line[1:])

        for _ in range(num):
            curr_pos = (curr_pos + sign) % 100
            if curr_pos == 0:
                result += 1

    print(f"Day 01, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
