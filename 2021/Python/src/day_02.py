from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_02.txt").read().splitlines()


def part_1():
    horizontal = 0
    depth = 0

    for line in file:
        dir, val = line.split()
        num = int(val)
        if dir == "forward":
            horizontal += num
        elif dir == "down":
            depth += num
        else:
            depth -= num

    print("Day 02, Part 1:", horizontal * depth)


def part_2():
    horizontal = 0
    aim = 0
    depth = 0

    for line in file:
        dir, val = line.split()
        num = int(val)
        if dir == "forward":
            horizontal += num
            depth += aim * num
        elif dir == "down":
            aim += num
        else:
            aim -= num

    print("Day 02, Part 2:", horizontal * depth)


if __name__ == "__main__":
    part_1()
    part_2()
