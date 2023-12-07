from pathlib import Path
from itertools import product

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


def if_five_of_a_kind(hand: str) -> int:
    if len(set(hand)) == 1:
        return 6000
    return 0


def is_four_of_a_kind(hand: str) -> int:
    counts = {x: hand.count(x) for x in hand}
    if 4 in counts.values():
        return 5000

    return 0


def is_full_house(hand: str) -> int:
    counts = {x: hand.count(x) for x in hand}
    if 3 in counts.values() and 2 in counts.values():
        return 4000

    return 0


def is_three_of_a_kind(hand: str) -> int:
    counts = {x: hand.count(x) for x in hand}
    if 3 in counts.values():
        return 3000

    return 0


def is_two_pairs(hand: str) -> int:
    counts = {x: hand.count(x) for x in hand}
    if list(counts.values()).count(2) == 2:
        return 2000

    return 0


def is_one_pair(hand: str) -> int:
    counts = {x: hand.count(x) for x in hand}
    if 2 in counts.values():
        return 1000

    return 0


def is_high_card(hand: str) -> int:
    return sum(map(lambda x: cards[x], hand))


def get_hand_power(hand: str) -> int:
    checks = (
        if_five_of_a_kind,
        is_four_of_a_kind,
        is_full_house,
        is_three_of_a_kind,
        is_two_pairs,
        is_one_pair,
    )

    for check in checks:
        power = check(hand)
        if power > 0:
            return power
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

    print("Day 07, Part 1", result)


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

    print("Day 07, Part 2", result)


if __name__ == "__main__":
    part_1()
    part_2()
