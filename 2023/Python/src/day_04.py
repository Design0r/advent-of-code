from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_04.txt").readlines()


def part_1():
    result = 0
    for line in file:
        left, right = line.strip().split(": ")[1].split(" | ")
        won = {int(i) for i in left.split(" ") if i != ""}
        played = {int(i) for i in right.split(" ") if i != ""}
        number_of_wins = len(won.intersection(played))
        points = int(2 ** (number_of_wins - 1))
        result += points

    print(f"Day 04, Part 1:", result)


def part_2():
    card_stack: dict[int, dict[str, int]] = {}

    for line in file:
        card_num = int(line.strip().split(": ")[0].split(" ")[-1])
        left, right = line.strip().split(": ")[1].split(" | ")
        won = {int(i) for i in left.split(" ") if i != ""}
        played = {int(i) for i in right.split(" ") if i != ""}
        number_of_wins = len(won.intersection(played))

        card_stack[card_num] = {"wins": number_of_wins, "count": 1}

    for card_id, card in card_stack.items():
        for _ in range(card["count"]):
            for i in range(card_stack[card_id]["wins"]):
                card_stack[card_id + i + 1]["count"] += 1

    result = sum([v["count"] for v in card_stack.values()])
    print(f"Day 04, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
