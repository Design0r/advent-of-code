from functools import reduce
from pathlib import Path

t, d = open(Path(__file__).parent.parent / "inputs/day_06.txt").read().splitlines()
time = [int(i) for i in t.split(":")[1].strip().split(" ") if i.isdigit()]
distance = [
    int(i) for i in d.split(":")[1].strip().split(" ") if i.isdigit()
]


def day_1():
    possible_wins = []
    for t, d in zip(time, distance):
        race = []
        for i in range(t + 1):
            if (t - i) * i > d:
                race.append((t - i) * i)
        possible_wins.append(len(race))

    result = reduce(lambda x, y: x * y, possible_wins)
    print("Day 06, Part 1:", result)


def day_2():
    possible_wins = 0
    joined_time = int("".join(str(i) for i in time))
    joined_distance = int("".join(str(i) for i in distance))

    for i in range(joined_time + 1):
        if (joined_time - i) * i > joined_distance:
            possible_wins += 1

    print("Day 06, Part 1:", possible_wins)


if __name__ == "__main__":
    day_1()
    day_2()
