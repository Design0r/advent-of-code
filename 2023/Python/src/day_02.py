file = open("inputs/day_02.txt").readlines()

RED = 12
GREEN = 13
BLUE = 14


def is_possible(play_sets: list[str], game_id: int) -> int:
    for i in play_sets:
        cubes = i.strip().split(", ")
        for cube in cubes:
            number, color = int(cube.split(" ")[0]), cube.split(" ")[1]
            if color == "red" and number > RED:
                return 0
            elif color == "green" and number > GREEN:
                return 0
            elif color == "blue" and number > BLUE:
                return 0
    return game_id


def get_set_power(play_sets: list[str]) -> int:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    for i in play_sets:
        cubes = i.strip().split(", ")
        for cube in cubes:
            number, color = int(cube.split(" ")[0]), cube.split(" ")[1]
            if color == "red" and number > max_cubes["red"]:
                max_cubes["red"] = number
            elif color == "green" and number > max_cubes["green"]:
                max_cubes["green"] = number
            elif color == "blue" and number > max_cubes["blue"]:
                max_cubes["blue"] = number

    return max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]


def part_1():
    games = []
    for idx, line in enumerate(file):
        line = line.strip()
        play_sets = line.split(":")[1].split(";")
        games.append(is_possible(play_sets, idx + 1))

    print(f"Day 02, Part 1: {sum(games)}")


def part_2():
    set_powers = []
    for line in file:
        line = line.strip()
        play_sets = line.split(":")[1].split(";")
        set_powers.append(get_set_power(play_sets))

    print(f"Day 02, Part 2: {sum(set_powers)}")


if __name__ == "__main__":
    part_1()
    part_2()
