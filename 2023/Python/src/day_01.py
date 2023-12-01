from typing import Optional

file = open("inputs/day_01.txt").readlines()

alpha_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part_1() -> None:
    numbers = []
    for line in file:
        line_nums = []
        for char in line:
            if char.isdigit():
                line_nums.append(int(char))

        line_num = int("".join(str(line_nums[0]) + str(line_nums[-1])))
        numbers.append(line_num)

    print(f"Day 01, Part 1: {sum(numbers)}")


def check_for_word_num(line: str, index: int) -> Optional[int]:
    for k, _ in alpha_num.items():
        num_len = len(k)
        input_chars = "".join(
            [i for idx, i in enumerate(line) if index <= idx <= index + num_len - 1]
        )

        if input_chars in alpha_num:
            return alpha_num[input_chars]

    return


def part_2() -> None:
    numbers = []
    for line in file:
        line_nums = []
        for i, char in enumerate(line):
            word_num = check_for_word_num(line, i)
            if char.isdigit():
                line_nums.append(int(char))
            elif word_num:
                line_nums.append(word_num)

        line_num = int("".join(str(line_nums[0]) + str(line_nums[-1])))
        numbers.append(line_num)

    print(f"Day 01, Part 2: {sum(numbers)}")


if __name__ == "__main__":
    part_1()
    part_2()
