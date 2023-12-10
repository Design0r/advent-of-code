from pathlib import Path
from typing import Generator
import math

file = open(Path(__file__).parent.parent / "inputs/day_08.txt").read()
base_instruction = file.split("\n\n")[0].strip()


def generate_instructions() -> Generator[str, None, None]:
    while True:
        for instruction in base_instruction:
            yield instruction


def day_1():
    nodes = {}
    for line in file.split("\n\n")[1].split("\n"):
        line = line.strip()
        node, elements = line.split(" = ")
        left, right = elements.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (left, right)

    number_of_steps = 0
    start = "AAA"
    end = "ZZZ"
    current = start

    instructions = generate_instructions()
    while current != end:
        instruction = next(instructions)
        if instruction == "L":
            current = nodes[current][0]
        elif instruction == "R":
            current = nodes[current][1]
        number_of_steps += 1

    print("Day 08, Part 1:", number_of_steps)


def solve(nodes, current: str) -> int:
    for idx, ins in enumerate(generate_instructions()):
        if "Z" in current:
            return idx
        if ins == "L":
            current = nodes[current][0]
        elif ins == "R":
            current = nodes[current][1]


def day_2():
    nodes = {}
    for line in file.split("\n\n")[1].split("\n"):
        line = line.strip()
        node, elements = line.split(" = ")
        left, right = elements.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (left, right)

    start = []
    end = set()

    for i in nodes.keys():
        if "A" in i:
            start.append(i)
        if "Z" in i:
            end.add(i)

    result = math.lcm(*[solve(nodes, s) for s in start])

    print("Day 08, Part 2:", result)


if __name__ == "__main__":
    day_1()
    day_2()
