from collections import defaultdict
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


def corners(dirs: list[Point]) -> int:
    """
    Count the number of corners, including inward-facing corners, based on the directions of edges.

    Args:
        dirs (list[Point]): A list of directions (edges) originating from a single point.

    Returns:
        int: The number of corners at the point, including inward-facing corners.
    """
    if len(dirs) < 2:
        return 0

    # Check all pairs of directions to see if they form a corner.
    corners_count = 0
    for i in range(len(dirs)):
        for j in range(i + 1, len(dirs)):
            dx1, dy1 = dirs[i]
            dx2, dy2 = dirs[j]

            # Check for perpendicularity (inward or outward corner)
            if (dx1 * dx2 + dy1 * dy2) == 0:  # Dot product == 0
                corners_count += 1

    return corners_count


def sides(edges: list[tuple[Point, Point]]) -> int:
    histogram: dict[Point, list[Point]] = defaultdict(list)

    for pos, dir in edges:
        histogram[pos].append(dir)

    for k, v in histogram.items():
        print(k, v)

    return sum(corners(v) for v in histogram.values())


@benchmark
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


@benchmark
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
