from pathlib import Path
from typing import NamedTuple

from utils import Vec2, benchmark


class Data(NamedTuple):
    cmds: str


def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_03.txt") as f:
        file = f.read().strip()
    return Data(file)


def calc(dir: str, curr: Vec2, seen: set[Vec2]) -> Vec2:
    if dir == "^":
        curr += (0, -1)
        seen.add(curr)
    elif dir == ">":
        curr += (1, 0)
        seen.add(curr)
    elif dir == "v":
        curr += (0, 1)
        seen.add(curr)
    else:
        curr += (-1, 0)
        seen.add(curr)

    return curr


@benchmark
def part_1(data: Data) -> None:
    curr = Vec2(0, 0)
    seen: set[Vec2] = {curr}
    for dir in data.cmds:
        curr = calc(dir, curr, seen)

    print(f"Day 03, Part 1: {len(seen)}")


@benchmark
def part_2(data: Data) -> None:
    robo_curr = Vec2(0, 0)
    santa_curr = Vec2(0, 0)
    robo_seen: set[Vec2] = {robo_curr}
    santa_seen: set[Vec2] = {santa_curr}
    toggle = True
    for dir in data.cmds:
        if toggle:
            santa_curr = calc(dir, santa_curr, santa_seen)
        else:
            robo_curr = calc(dir, robo_curr, robo_seen)
        toggle = not toggle

    result = len(robo_seen.union(santa_seen))
    print(f"Day 03, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
