from pathlib import Path

from utils import benchmark

with open(Path(__file__).parent.parent / "samples/day_12.txt") as f:
    file = f.read().strip().splitlines()

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))
Point = tuple[int, int]
Region = tuple[str, int, set[Point]]


def area(point: Point, visited: set[Point]) -> Region:
    value = file[point[1]][point[0]]
    if point in visited:
        return value, 0, set()

    visited.add(point)
    region = {point}
    area = 1
    todo = [point]

    while todo:
        p = todo.pop()

        for dir in DIRS:
            next = p[0] + dir[0], p[1] + dir[1]
            if not (0 <= next[0] < len(file[0]) and 0 <= next[1] < len(file)):
                continue

            if next in region:
                continue

            next_val = file[next[1]][next[0]]

            if next_val == value:
                visited.add(next)
                region.add(next)
                area += 1
                todo.append(next)

    return value, area, region


def perimeter(value: str, region: set[Point]) -> tuple[int, list[tuple[Point, Point]]]:
    counter = 0
    sides: list[tuple[Point, Point]] = []

    for dir in DIRS:
        for p in region:
            next = p[0] + dir[0], p[1] + dir[1]
            if not (0 <= next[0] < len(file[0]) and 0 <= next[1] < len(file)):
                counter += 1
                sides.append((p, dir))
                continue

            next_val = file[next[1]][next[0]]
            if value != next_val:
                sides.append((p, dir))
                counter += 1

    return counter, sides


        return 0

    # Check all pairs of directions to see if they form a corner.
def sides(edges: list[tuple[Point, Point]]) -> int:
    counter = 0

    for i, (p, d) in enumerate(edges):
        if i + 1 >= len(edges):
            counter += 1
            return counter
        next_p, next_d = edges[i + 1]
        if d == next_d and (p[0] == next_p[0] or p[1] == next_p[1]):
            continue
        counter += 1

    return counter


@benchmark("finished in: ")
def part_1() -> None:
    result = 0
    visited: set[Point] = set()

    for y, row in enumerate(file):
        for x, _ in enumerate(row):
            val, area_size, region = area((x, y), visited)
            if area_size > 0:
                peri, _ = perimeter(val, region)
                result += area_size * peri

    print(f"Day 12, Part 1: {result}")


@benchmark("finished in: ")
def part_2() -> None:
    result = 0
    visited: set[Point] = set()

    for y, row in enumerate(file):
        for x, _ in enumerate(row):
            val, area_size, region = area((x, y), visited)
            if area_size > 0:
                _, side_pts = perimeter(val, region)
                num_sides = sides(side_pts)
                print(val, num_sides)
                result += num_sides * area_size
    print(f"Day 12, Part 2: {result}")


if __name__ == "__main__":
    part_1()
    part_2()
