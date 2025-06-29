from pathlib import Path
from typing import NamedTuple

from utils import benchmark


class Data(NamedTuple):
    lines: list[str]


def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_05.txt") as f:
        file = f.read().strip().splitlines()
    return Data(file)


def contains_three_vowels(input: str) -> bool:
    counter = 0
    for i in input:
        for v in "aeiou":
            if i == v:
                counter += 1
                continue

    return counter >= 3


def contains_double_letter(input: str) -> bool:
    for idx, i in enumerate(input):
        if idx >= len(input) - 1:
            break
        if i == input[idx + 1]:
            return True

    return False


def doesnt_contain_bad_strings(input: str, bad_strings: list[str]) -> bool:
    for b in bad_strings:
        if b in input:
            return False

    return True


@benchmark
def part_1(data: Data) -> None:
    result = 0
    for i in data.lines:
        if all(
            (
                contains_three_vowels(i),
                contains_double_letter(i),
                doesnt_contain_bad_strings(i, ["ab", "cd", "pq", "xy"]),
            )
        ):
            result += 1
    print(f"Day 05, Part 1: {result}")


def part_2(data: Data) -> None:
    result = 0
    print(f"Day 05, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
