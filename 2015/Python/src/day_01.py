from pathlib import Path
from collections import Counter

with open(Path(__file__).parent.parent / "inputs/day_01.txt") as f:
    file = f.read().strip()


def part_1() -> None:
    counter = Counter(file)
    result = counter["("] - counter[")"]

    print(f"Day 1, Part 1: {result}")


def part_2() -> None:
    counter = 0
    result = 0
    for idx, i in enumerate(file, 1):
        counter += 1 if i == "(" else -1
        if counter == -1:
            result = idx
            break

    print(f"Day 1, Part 2: {result}")


if __name__ == "__main__":
    part_1()
    part_2()
