import ast
import math
from functools import cmp_to_key
from typing import List


def convert_to_list(*lists: str) -> List[int]:
    return [ast.literal_eval(i) for i in lists]


def compare_list(l, r) -> int:
    match l, r:
        case list(), list():
            for l2, r2 in zip(l, r):
                if (res := compare_list(l2, r2)) != 0:
                    return res

            if len(l) - len(r) < 0:
                return -1
            elif len(l) - len(r) > 0:
                return 1
            else:
                return 0

        case list(), int():
            return compare_list(l, [r])

        case int(), list():
            return compare_list([l], r)

        case int(), int():
            if l < r:
                return -1
            elif l > r:
                return 1
            else:
                return 0


def part_one():
    result = 0
    for i, section in enumerate(signal_pairs, start=1):
        pair = convert_to_list(*section.split("\n"))
        result += i if compare_list(*pair) == -1 else 0

    return result


def part_two() -> int:
    added_data = [[[2]], [[6]]]
    data = [*added_data]

    for section in signal_pairs:
        data.extend([ast.literal_eval(i) for i in section.splitlines()])

    data.sort(key=cmp_to_key(compare_list))
    result = math.prod([i for i, v in enumerate(data, start=1) if v in added_data])
    return result


if __name__ == "__main__":
    signal_pairs = open("input.txt").read().split("\n\n")

    print(f"Part One: {part_one()}")
    print(f"Part Two: {part_two()}")
