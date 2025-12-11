from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path

from utils import benchmark


@dataclass(slots=True)
class Machine:
    lights: str
    buttons: list[tuple[int, ...]]
    joltage: tuple[int, ...]


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
            joltage = tuple(map(int, j[1:-1].split(",")))
            machines.append(Machine(lgt[1:-1], buttons, joltage))

    return Data(machines)


def push_button(lights: str, buttons: tuple[int, ...]) -> str:
    lgt = [lgt for lgt in lights]
    for b in buttons:
        lgt[b] = "#" if lights[b] == "." else "."

    return "".join(lgt)


def push_button_jolt(
    joltage: tuple[int, ...], buttons: tuple[int, ...]
) -> tuple[int, ...]:
    jlt = [j for j in joltage]
    for b in buttons:
        jlt[b] += 1

    return tuple(jlt)


def calc(machine: Machine):
    goal = machine.joltage
    buttons = machine.buttons
    button_presses = 0
    curr_joltage: set[tuple[int, ...]] = set([tuple([0 for _ in goal])])

    while True:
        curr_joltage = {
            push_button_jolt(jlt, btn) for jlt in curr_joltage for btn in buttons
        }

        button_presses += 1

        if goal in curr_joltage:
            print(f"completed {machine}")
            return button_presses


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
    with ProcessPoolExecutor() as p:
        results = p.map(calc, data.machines)

    result = sum(results)
    print(f"Day 10, Part 2: {result}")


if __name__ == "__main__":
    data = parse()
    part_1(data)
    part_2(data)
