from pathlib import Path
from typing import NamedTuple, Optional

Point = tuple[int, int]
SPAWN = (500, 0)
DOWN = (0, 1)
DIAG_L = (-1, 1)
DIAG_R = (1, 1)


def move(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1])


class Data(NamedTuple):
    lines: list[str]
    instructions: list[list[Point]]


def parse() -> Data:
    inst: list[list[Point]] = []
    with open(Path(__file__).parent.parent / "inputs/day_14.txt") as f:
        file = f.read().strip().splitlines()
        for line in file:
            t: list[Point] = []
            for coord in line.split(" -> "):
                x, y = coord.split(",")
                t.append((int(x), int(y)))
            inst.append(t)

    return Data(file, inst)


def build_stones(instr: list[list[Point]]) -> set[Point]:
    s: set[Point] = set()
    for line in instr:
        for i, p in enumerate(line):
            s.add(p)
            if i + 1 >= len(line):
                break
            next = line[i + 1]
            if p[0] == next[0]:
                nums = nums_between(p[1], next[1])
                for y in nums:
                    s.add((p[0], y))
            else:
                nums = nums_between(p[0], next[0])
                for x in nums:
                    s.add((x, p[1]))

    return s


def nums_between(a: int, b: int) -> list[int]:
    low = min(a, b)
    high = max(a, b)
    return [low + i for i in range(high - low)]


def simulate(
    start: Point, collisions: set[Point], max_depth: int, floor: Optional[int] = None
) -> Optional[Point]:
    curr = start
    if floor:
        while True:
            if (p := move(curr, DOWN)) not in collisions and p[1] < floor:
                curr = p
            elif (p := move(curr, DIAG_L)) not in collisions and p[1] < floor:
                curr = p
            elif (p := move(curr, DIAG_R)) not in collisions and p[1] < floor:
                curr = p
            elif curr == start:
                return None
            else:
                collisions.add(curr)
                return curr

    while True:
        if (p := move(curr, DOWN)) not in collisions and p[1] < max_depth:
            curr = p
        elif (p := move(curr, DIAG_L)) not in collisions and p[1] < max_depth:
            curr = p
        elif (p := move(curr, DIAG_R)) not in collisions and p[1] < max_depth:
            curr = p
        elif curr[1] + 1 >= max_depth:
            return None
        else:
            collisions.add(curr)
            return curr


def part_1(data: Data) -> None:
    result = 0
    collisions = build_stones(data.instructions)
    sand: set[Point] = set()
    max_depth = max(collisions, key=lambda x: x[1])[1] + 1
    while True:
        res = simulate(SPAWN, collisions, max_depth)
        if not res:
            break

        sand.add(res)
        result += 1

    # print_simulation(collisions, sand)
    print(f"Day 14, Part 1: {result}")


def print_simulation(stones: set[Point], sand: set[Point]):
    x_min = min(stones, key=lambda x: x[0])[0]
    x_max = max(stones, key=lambda x: x[0])[0]
    y_max = max(stones, key=lambda x: x[1])[1]

    grid = [["." for _ in range(x_max - x_min + 1)] for _ in range(y_max + 1)]
    for p in stones:
        x = p[0] - x_min
        y = p[1]
        grid[y][x] = "\033[91m#\033[0m"

    for s in sand:
        x = s[0] - x_min
        y = s[1]
        grid[y][x] = "\033[92mo\033[0m"

    for line in grid:
        print("".join(line))


def part_2(data: Data) -> None:
    result = 0
    collisions = build_stones(data.instructions)
    sand: set[Point] = set()
    floor = max(collisions, key=lambda x: x[1])[1] + 2
    max_depth = floor + 1

    while True:
        res = simulate(SPAWN, collisions, max_depth, floor=floor)
        if not res:
            result += 1
            sand.add(SPAWN)
            break

        sand.add(res)
        result += 1

    # print_simulation(collisions, sand)
    print(f"Day 14, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
