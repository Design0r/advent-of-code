import math


class Monkey:
    def __init__(self, input: str):

        self.watch_counter = 0

        for line in input.split("\n"):
            line = line.strip()
            if line.startswith("Monkey"):
                self.number = int(line.split(" ")[-1][:-1])
            elif line.startswith("Starting"):
                self.items = list(map(int, line.split(":")[-1].strip().split(", ")))
            elif line.startswith("Operation"):
                self.symbol = line.split("=")[-1].strip().split(" ")[1]
                self.operator = line.split("=")[-1].strip().split(" ")[-1]
            elif line.startswith("Test"):
                self.divisor = int(line.split(" ")[-1])
            elif line.startswith("If true:"):
                self.true_monkey = int(line.split(" ")[-1])
            elif line.startswith("If false:"):
                self.false_monkey = int(line.split(" ")[-1])


def calc(rounds: int, part_1: bool = None, part_2: bool = None) -> int:
    file = open("input.txt").read().split("\n\n")
    monkeys = [Monkey(i) for i in file]
    lcm = math.lcm(*[m.divisor for m in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.watch_counter += 1
                curr_level = int(item)
                if monkey.symbol == "+":
                    if monkey.operator == "old":
                        curr_level += curr_level
                    else:
                        curr_level += int(monkey.operator)
                elif monkey.symbol == "*":
                    if monkey.operator == "old":
                        curr_level *= curr_level
                    else:
                        curr_level *= int(monkey.operator)

                if part_1:
                    curr_level //= 3
                elif part_2:
                    curr_level %= lcm

                if curr_level % monkey.divisor == 0:
                    monkeys[monkey.true_monkey].items.append(curr_level)
                else:
                    monkeys[monkey.false_monkey].items.append(curr_level)

            monkey.items = []

    s = sorted(monkeys, key=lambda x: x.watch_counter, reverse=True)
    return math.prod(i.watch_counter for i in s[:2])


if __name__ == '__main__':
    print(f"Part 1: {calc(20, part_1=True)}")
    print(f"Part 2: {calc(10000, part_2=True)}")
