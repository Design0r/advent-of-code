from itertools import batched
from multiprocessing import Pool
from pathlib import Path
from typing import Iterator

file = open(Path(__file__).parent.parent / "inputs/day_05.txt").read()


maps = file.split("\n\n")


def apply_seed_map(seed: int, map_vals):
    d_start, s_start, length = map_vals
    if seed < s_start or (s_start + length) < seed:
        return seed

    return d_start - s_start + seed


def part_1():
    seeds = map(int, file.split("\n")[0].split(": ")[1].split(" "))
    result = []

    for seed in seeds:
        mapped_val = seed
        for m in maps:
            m = m.split("\n")
            m.pop(0)

            rows = [(j) for i in m for j in i.split("\n")]
            for row in rows:
                map_vals = tuple(map(int, row.split(" ")))
                returned = apply_seed_map(mapped_val, map_vals)
                if returned != mapped_val:
                    mapped_val = returned
                    break
        result.append(mapped_val)

    print("Day 05, Part 1", min(result))


def generate_seeds(seeds: Iterator):
    seed_list = []

    for seed, length in batched(seeds, 2):
        seed_list.extend(range(seed, seed + length))

    return seed_list


def multiprocess(seed_grp):
    start, length = seed_grp
    seeds = range(start, start + length)
    minimum = 100_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000

    maps_processed = []
    for m in maps:
        m = m.split("\n")
        m.pop(0)
        rows = (j for i in m for j in i.split("\n"))
        map_vals = [tuple(map(int, row.split(" "))) for row in rows]
        maps_processed.append(map_vals)

    for seed in seeds:
        mapped_val = seed
        for map_vals in maps_processed:
            for map_val in map_vals:
                returned = apply_seed_map(mapped_val, map_val)
                if returned != mapped_val:
                    mapped_val = returned
                    break
        minimum = min(minimum, mapped_val)

    return minimum


def part_2():
    seed_ranges = map(int, file.split("\n")[0].split(": ")[1].split(" "))
    seed_ranges = batched(seed_ranges, 2)

    with Pool(processes=10) as pool:
        results = pool.imap_unordered(multiprocess, seed_ranges)
        print("Day 05, Part 2", min(results))


if __name__ == "__main__":
    part_1()
    part_2()
