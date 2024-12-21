from pathlib import Path
from typing import NamedTuple

from utils import benchmark

Point = tuple[int, int]


class Game(NamedTuple):
    ButtonA: Point
    ButtonB: Point
    Prize: Point


@benchmark
def parse() -> list[Game]:
    with open(Path(__file__).parent.parent / "inputs/day_13.txt") as f:
        file = f.read().strip()

    def _extraxt(line: str) -> Point:
        nums = [int(x[2:]) for x in line.split(": ")[1].split(", ")]
        return nums[0], nums[1]

    return [
        Game(*[_extraxt(s) for s in sets.splitlines()]) for sets in file.split("\n\n")
    ]


def sim(game: Game) -> list[int]:
    solutions: list[int] = []
    for a in range(100, 0, -1):
        for b in range(100, 0, -1):
            res = game.ButtonA[0] * a, game.ButtonA[1] * a
            res = res[0] + game.ButtonB[0] * b, res[1] + game.ButtonB[1] * b
            if res[0] == game.Prize[0] and res[1] == game.Prize[1]:
                solutions.append(a * 3 + b)
            if res[0] < game.Prize[0] or res[1] < game.Prize[1]:
                break

    return solutions


def solve_by_elimination(game: Game, muliply_target: int = 1) -> int:
    """
    94*A + 22*B = 8400
    34*A + 67*B = 5400

    34 * (94*A) + 34 * (22*B) = 8400*34
    94 * (34*A) + 94 * (67*B) = 5400*94

    B * (34*22 - 94*67) = 8400*34 - 5400*94
    B = (8400*34 - 5400*94) / (34*22 - 94*67)

    A = (8400 - 22*B) / 94
    """
    btn_a_x, btn_a_y = game.ButtonA
    btn_b_x, btn_b_y = game.ButtonB
    prize_x, prize_y = game.Prize[0] + muliply_target, game.Prize[1] + muliply_target

    B = (prize_x * btn_a_y - prize_y * btn_a_x) / (
        btn_a_y * btn_b_x - btn_a_x * btn_b_y
    )
    if not B.is_integer() or B < 0:
        return 0

    A = (prize_x - btn_b_x * B) / (btn_a_x)
    if not A.is_integer() or A < 0:
        return 0

    return int(A) * 3 + int(B)


@benchmark
def part_1(data: list[Game]) -> None:
    result = sum(min(x) for game in data if (x := sim(game)))
    print(f"Day 13, Part 1: {result}")


@benchmark
def part_2(data: list[Game]) -> None:
    result = sum(
        solve_by_elimination(game, muliply_target=10000000000000) for game in data
    )
    print(f"Day 13, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
