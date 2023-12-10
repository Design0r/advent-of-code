from pathlib import Path
from typing import Generator

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


def day_2():
    nodes = {}
    for line in file.split("\n\n")[1].split("\n"):
        line = line.strip()
        node, elements = line.split(" = ")
        left, right = elements.replace("(", "").replace(")", "").split(", ")
        nodes[node] = (left, right)

    number_of_steps = 0
    start = []
    end = set()
    current = start

    for i in nodes.keys():
        if "A" in i:
            start.append(i)
        if "Z" in i:
            end.add(i)

    instructions = generate_instructions()
    while True:
        instruction = next(instructions)

        for idx, i in enumerate(start):
            if instruction == "L":
                current[idx] = nodes[i][0]
            elif instruction == "R":
                current[idx] = nodes[i][1]

        number_of_steps += 1
        if set(current) == end:
            break

        if number_of_steps % 1_000_000 == 0:
            print(number_of_steps)
    print("Day 08, Part 2:", number_of_steps)


if __name__ == "__main__":
    # day_1()
    day_2()
