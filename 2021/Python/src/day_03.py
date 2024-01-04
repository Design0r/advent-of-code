from pathlib import Path
from copy import deepcopy

file = open(Path(__file__).parent.parent / "samples/day_03.txt").read().splitlines()


def part_1():
    grid = list(zip(*file))

    gamma = []
    epsilon = []

    for col in grid:
        count = {k: col.count(k) for k in col}

        if count["0"] > count["1"]:
            gamma.append("0")
            epsilon.append("1")
            continue

        gamma.append("1")
        epsilon.append("0")

    print(
        "Day 03, Part 1:", int("".join(gamma), base=2) * int("".join(epsilon), base=2)
    )


def part_2():
    grid = list(zip(*file))
    major = deepcopy(file)
    minor = deepcopy(file)
    for idx, col in enumerate(file):
        count = {k: col.count(k) for k in grid[idx]}

        if count["0"] > count["1"]:
            if len(major) > 1:
                major = [i for i in major if i[idx] == "0"]
            if len(minor) > 1:
                minor = [i for i in minor if i[idx] == "1"]
        elif count["1"] > count["0"]:
            if len(major) > 1:
                major = [i for i in major if i[idx] == "1"]
            if len(minor) > 1:
                minor = [i for i in minor if i[idx] == "0"]
        else:
            if len(major) > 1:
                major = [i for i in major if i[idx] == "1"]
            if len(minor) > 1:
                minor = [i for i in minor if i[idx] == "0"]
        print(major, minor)


if __name__ == "__main__":
    part_1()
    part_2()
