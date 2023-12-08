from itertools import count, product
from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_07.txt").readlines()
cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def get_hand_power(hand: str) -> int:
    counts = {x: hand.count(x) for x in hand}
    vals = counts.values()

    if len(set(hand)) == 1:
        return 6
    elif 4 in vals:
        return 5
    elif 3 in vals and 2 in vals:
        return 4
    elif 3 in vals:
        return 3
    elif list(vals).count(2) == 2:
        return 2
    elif 2 in vals:
        return 1

    return 0


def part_1():
    hands = []
    for line in file:
        line = line.strip()
        hand, bid = line.split(" ")[0], int(line.split(" ")[1])

        hands.append((hand, bid, get_hand_power(hand)))

    result = 0
    for idx, (_, bid, _) in enumerate(
        sorted(
            hands,
            key=lambda x: (
                x[2],
                cards[x[0][0]],
                cards[x[0][1]],
                cards[x[0][2]],
                cards[x[0][3]],
                cards[x[0][4]],
            ),
        )
    ):
        result += (idx + 1) * bid

    print("Day 07, Part 1:", result)


def part_2():
    cards["J"] = 1
    hands = []
    for line in file:
        points = []

        line = line.strip()
        hand, bid = line.split(" ")[0], int(line.split(" ")[1])
        joker_index = [idx for idx, x in enumerate(hand) if x == "J"]

        if not joker_index:
            hands.append((hand, bid, get_hand_power(hand)))
            continue

        combinations = product(cards.keys(), repeat=len(joker_index))

        for idx in combinations:
            temp_hand = list(hand)
            for i, k in zip(joker_index, idx):
                temp_hand[i] = k
                joined = "".join(temp_hand)
                points.append((joined, get_hand_power(joined)))

        if points:
            sorted_points = sorted(
                points,
                key=lambda x: (
                    x[1],
                    cards[x[0][0]],
                    cards[x[0][1]],
                    cards[x[0][2]],
                    cards[x[0][3]],
                    cards[x[0][4]],
                ),
            )
            hands.append((hand, bid, sorted_points[-1][1]))

    result = 0
    for idx, (_, bid, _) in enumerate(
        sorted(
            hands,
            key=lambda x: (
                x[2],
                cards[x[0][0]],
                cards[x[0][1]],
                cards[x[0][2]],
                cards[x[0][3]],
                cards[x[0][4]],
            ),
        )
    ):
        result += (idx + 1) * bid

    print("Day 07, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
