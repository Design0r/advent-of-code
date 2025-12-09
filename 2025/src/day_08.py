from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from pathlib import Path

from utils import Vec3, benchmark


@dataclass(slots=True)
class Data:
    edges: list[tuple[int, Vec3, Vec3]]
    boxes: list[Vec3]


@benchmark
def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_08.txt") as f:
        file = f.read().strip().splitlines()

    boxes = [Vec3(*[int(n) for n in line.split(",")]) for line in file]
    edges: list[tuple[int, Vec3, Vec3]] = []

    for a, b in combinations(boxes, 2):
        distance = a.distance_squared(b)
        edges.append((distance, a, b))

    edges.sort(key=lambda e: e[0])

    return Data(edges, boxes)


type Connection = tuple[Vec3, Vec3]


@benchmark
def part_1(data: Data) -> None:
    circuits: list[set[Vec3]] = []
    for _, a, b in data.edges[:1000]:
        ca = cb = None

        for c in circuits:
            if a in c:
                ca = c
            if b in c:
                cb = c

        if not ca and not cb:
            circuits.append({a, b})
        elif ca and not cb:
            ca.add(b)
        elif not ca and cb:
            cb.add(a)
        elif ca is cb:
            pass
        elif ca and cb:
            ca.update(cb)
            circuits.remove(cb)

    result = reduce(
        lambda acc, curr: acc * len(curr),
        sorted(circuits, key=lambda x: -len(x))[:3],
        1,
    )

    print(f"Day 08, Part 1: {result}")


@benchmark
def part_2(data: Data) -> None:
    result = 0
    edges = data.edges

    circuits: list[set[Vec3]] = []
    for idx, (_, a, b) in enumerate(edges):
        ca = cb = None

        for c in circuits:
            if a in c:
                ca = c
            if b in c:
                cb = c

        if circuits and len(circuits[0]) == len(data.boxes):
            _, x, y = edges[idx - 1]
            result = x.x * y.x
            break

        if not ca and not cb:
            circuits.append({a, b})
        elif ca and not cb:
            ca.add(b)
        elif not ca and cb:
            cb.add(a)
        elif ca is cb:
            continue
        elif ca and cb:
            ca.update(cb)
            circuits.remove(cb)

    print(f"Day 08, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
