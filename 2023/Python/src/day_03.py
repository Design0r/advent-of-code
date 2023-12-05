from functools import reduce
from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_03.txt").readlines()


def get_part_number_sum(line_idx: int) -> int:
    part_numbers = []
    temp_list = []
    start_idx = 0
    curr_line = file[line_idx].strip()

    return_list = []
    for idx, i in enumerate(curr_line):
        if i.isdigit():
            if not temp_list:
                start_idx = idx
            temp_list.append(i)

            if idx == len(curr_line) - 1:
                part_numbers.append([start_idx, len(temp_list), "".join(temp_list)])
        elif temp_list:
            part_numbers.append([start_idx, len(temp_list), "".join(temp_list)])
            temp_list = []

    for start, length, num in part_numbers:
        end = start + length
        bounds_l = start - 1 if start > 0 else start
        bounds_r = end if end < len(curr_line) else end - 1
        bounds_t = line_idx - 1 if line_idx > 0 else line_idx
        bounds_b = line_idx + 1 if line_idx < len(file) - 1 else line_idx

        bounds: list[str] = (
            file[bounds_t][bounds_l : bounds_r + 1]
            + file[bounds_b][bounds_l : bounds_r + 1]
            + curr_line[bounds_l]
            + curr_line[bounds_r]
        )

        filtered = list(filter(lambda x: not x.isdigit() and x != ".", bounds))
        if filtered:
            return_list.append(int(num))

    return sum(return_list)


def get_gear_positions(line_idx: int) -> list[tuple[int, tuple[int, int]]]:
    part_numbers = []
    temp_list = []
    start_idx = 0
    curr_line = file[line_idx].strip()

    gears = []
    for idx, i in enumerate(curr_line):
        if i.isdigit():
            if not temp_list:
                start_idx = idx
            temp_list.append(i)

            if idx == len(curr_line) - 1:
                part_numbers.append([start_idx, len(temp_list), "".join(temp_list)])
        elif temp_list:
            part_numbers.append([start_idx, len(temp_list), "".join(temp_list)])
            temp_list = []

    for start, length, num in part_numbers:
        end = start + length
        bounds_l = start - 1 if start > 0 else start
        bounds_r = end if end < len(curr_line) else end - 1
        bounds_t = line_idx - 1 if line_idx > 0 else line_idx
        bounds_b = line_idx + 1 if line_idx < len(file) - 1 else line_idx

        for pos, i in enumerate(file[bounds_t][bounds_l : bounds_r + 1]):
            if i == "*":
                gears.append(((line_idx - 1, pos + bounds_l), num))
        for pos, i in enumerate(file[bounds_b][bounds_l : bounds_r + 1]):
            if i == "*":
                gears.append(((line_idx + 1, pos + bounds_l), num))
        if curr_line[bounds_l] == "*":
            gears.append(((line_idx, bounds_l), num))
        if curr_line[bounds_r] == "*":
            gears.append(((line_idx, bounds_r), num))

    return gears


def part_01():
    part_number_sum = []
    for idx, _ in enumerate(file):
        part_number_sum.append(get_part_number_sum(idx))

    print("Day 03, Part 1:", sum(part_number_sum))


def convert_to_dict_list(tuples_list):
    result_dict = {}
    for key, value in tuples_list:
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
    return [{k: v} for k, v in result_dict.items()]


def part_02():
    gear_sum: list[tuple[int, tuple[int, int]]] = []
    for idx, _ in enumerate(file):
        gear_sum.extend(get_gear_positions(idx))

    gears = []
    dict_list = convert_to_dict_list(gear_sum)

    for d in dict_list:
        for k, v in d.items():
            if len(v) == 2:
                gears.append(reduce(lambda x, y: int(x) * int(y), v))
    print("Day 03, Part 2:", sum(gears))


if __name__ == "__main__":
    part_01()
    part_02()
