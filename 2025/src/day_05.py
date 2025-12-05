import gc

gc.freeze()


def parse() -> tuple[list[tuple[int, int]], list[int]]:
    f = open("inputs/day_05.txt")
    ranges_raw, ingredients_raw = f.read().split("\n\n")

    ranges = [tuple(map(int, line.split("-"))) for line in ranges_raw.splitlines()]
    ranges.sort(key=lambda x: x[0])

    ingredients = [int(i) for i in ingredients_raw.splitlines()]

    return (merge(ranges), ingredients)


def merge(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    for start, end in ranges:
        if merged:
            last_start, last_end = merged[-1]
            if start <= last_end:
                if end > last_end:
                    merged[-1] = (last_start, end)
            else:
                merged.append((start, end))
        else:
            merged.append((start, end))

    return merged


def part_1(ranges: list[tuple[int, int]], items: list[int]) -> None:
    result = 0

    for min, max in ranges:
        for item in items:
            if min <= item and item <= max:
                result += 1
                break

    print(f"Day 05, Part 1: {result}")


def part_2(ranges: list[tuple[int, int]]) -> None:
    result = 0
    for min, max in ranges:
        result += max + 1 - min

    print(f"Day 05, Part 2: {result}")


ranges, items = parse()
part_1(ranges, items)
part_2(ranges)
