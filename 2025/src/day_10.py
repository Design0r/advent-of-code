from dataclasses import dataclass
from pathlib import Path

from utils import benchmark


@dataclass(slots=True)
class Machine:
    lights: str
    buttons: list[tuple[int, ...]]
    joltage: list[int]


@dataclass(slots=True)
class Data:
    machines: list[Machine]


@benchmark
def parse() -> Data:
    with open(Path(__file__).parent.parent / "inputs/day_10.txt") as f:
        file = f.read().strip().splitlines()
        machines: list[Machine] = []

        for line in file:
            lgt, *b, j = line.split()
            buttons = [tuple(map(int, button[1:-1].split(","))) for button in b]
            joltage = list(map(int, j[1:-1].split(",")))
            machines.append(Machine(lgt[1:-1], buttons, joltage))

    return Data(machines)


def push_button(lights: str, buttons: tuple[int, ...]) -> str:
    lgt = [lgt for lgt in lights]
    for b in buttons:
        lgt[b] = "#" if lights[b] == "." else "."

    return "".join(lgt)


@benchmark
def part_1(data: Data) -> None:
    result = 0

    for machine in data.machines:
        button_presses = 0
        curr_lights: set[str] = set(["".join(["." for _ in machine.lights])])

        while True:
            curr_lights = {
                push_button(lgt, btn) for lgt in curr_lights for btn in machine.buttons
            }

            button_presses += 1

            if machine.lights in curr_lights:
                break

        result += button_presses

    print(f"Day 10, Part 1: {result}")


@benchmark
def part_2(data: Data) -> None:
    result = 0
    print(f"Day 10, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
