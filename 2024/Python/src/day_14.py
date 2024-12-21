from __future__ import annotations

from copy import copy
from functools import reduce
from pathlib import Path
from typing import NamedTuple

from utils import Vec2, benchmark

Grid = list[list[Vec2]]

DIRS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


class Robot(NamedTuple):
    pos: Vec2
    vel: Vec2

    def move(self, times: int, dimensions: Vec2) -> Robot:
        temp = self.pos + (self.vel * times)
        new = Vec2(temp.x % dimensions.x, temp.y % dimensions.y)
        return self._replace(pos=new)

    def __copy__(self) -> Robot:
        return Robot(Vec2(**self.pos._asdict()), Vec2(**self.vel._asdict()))


class Data(NamedTuple):
    robots: list[Robot]


@benchmark
def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_14.txt") as f:
        file = f.read().strip().splitlines()

    def _extract(line: str) -> Robot:
        p, v = line.split(" ")
        p = [int(x) for x in p[2:].split(",")]
        v = [int(x) for x in v[2:].split(",")]
        return Robot(Vec2(*p), Vec2(*v))

    robots = [_extract(line) for line in file]

    return Data(robots)


def mul_quads(robots: list[Robot], dim: Vec2) -> int:
    quadrants = [0, 0, 0, 0]
    h_mid = dim.x // 2
    v_mid = dim.y // 2

    for robot in robots:
        if robot.pos.x < h_mid and robot.pos.y < v_mid:
            quadrants[0] += 1
        elif robot.pos.x > h_mid and robot.pos.y < v_mid:
            quadrants[1] += 1
        elif robot.pos.x < h_mid and robot.pos.y > v_mid:
            quadrants[2] += 1
        elif robot.pos.x > h_mid and robot.pos.y > v_mid:
            quadrants[3] += 1
    print(quadrants)

    return reduce(lambda x, y: x * y, quadrants)


def is_tree(robots: list[Robot]) -> bool:
    r_set = {r.pos for r in robots}
    for r in r_set:
        counter = 0
        for dir in DIRS:
            new_pos = r + dir
            if new_pos in r_set:
                counter += 1
            else:
                continue

        if counter == 8:
            return True

    return False


def print_grid(robots: list[Robot], dimensions: Vec2, quad: bool = False):
    for y in range(dimensions.y):
        line: list[str] = []
        if quad:
            if y == dimensions.y // 2:
                print()
                continue
        for x in range(dimensions.x):
            if quad:
                if x == dimensions.x // 2:
                    line.append(" ")
                    continue
            count = 0
            for r in robots:
                if r.pos == Vec2(x, y):
                    count += 1
            line.append(str(count) if count > 0 else ".")
        print("".join(line))
    print()


@benchmark
def part_1(data: Data) -> None:
    result = 0
    robots = copy(data.robots)
    dimensions = Vec2(101, 103)

    new_robots = [robot.move(100, dimensions) for robot in robots]
    result = mul_quads(new_robots, dimensions)
    print(f"Day 14, Part 1: {result}")


@benchmark
def part_2(data: Data) -> None:
    result = 0
    dimensions = Vec2(101, 103)
    i = 1
    while True:
        new_robots = [robot.move(i, dimensions) for robot in data.robots]

        if is_tree(new_robots):
            result = i
            # print_grid(new_robots, dimensions)
            break

        i += 1
    print(f"Day 14, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
