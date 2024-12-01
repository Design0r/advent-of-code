from pathlib import Path

with open(Path(__file__).parent.parent / "inputs/day_02.txt") as f:
    file = f.read().strip()


def part_1() -> None:
    result = 0
    for i in file.splitlines():
        l, w, h = [int(i) for i in i.split("x")]
        x, y, z = l * w, w * h, h * l
        result += 2 * x + 2 * y + 2 * z + (min(x, y, z))

    print(f"Day 2, Part 1: {result}")


def part_2() -> None:
    result = 0
    for i in file.splitlines():
        l, w, h = [int(i) for i in i.split("x")]
        result += 2 * l + 2 * w + l * w * h

    print(f"Day 2, Part 2: {result}")


if __name__ == "__main__":
    part_1()
    part_2()
