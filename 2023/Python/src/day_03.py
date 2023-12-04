import functools
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


def get_gear_sum(row_idx: int) -> int:
    curr_row = file[row_idx].strip()

    result = []
    star_indices = []

    for star_idx, i in enumerate(curr_row):
        if i == "*":
            star_indices.append(star_idx)

    for star_idx in star_indices:
        found_numbers = set()
        bounds_l = star_idx - 1
        bounds_r = star_idx + 1
        bounds_t = row_idx - 1
        bounds_b = row_idx + 1

        top_row = file[bounds_t].strip()
        bottom_row = file[bounds_b].strip()

        if file[bounds_t][bounds_l].isdigit():
            number = scan_for_number(top_row, bounds_l)
            found_numbers.add(number)
        if file[bounds_t][star_idx].isdigit():
            number = scan_for_number(top_row, star_idx)
            found_numbers.add(number)
        if file[bounds_t][bounds_r].isdigit():
            number = scan_for_number(top_row, bounds_r)
            found_numbers.add(number)

        if file[bounds_b][bounds_l].isdigit():
            number = scan_for_number(bottom_row, bounds_l)
            found_numbers.add(number)
        if file[bounds_b][star_idx].isdigit():
            number = scan_for_number(bottom_row, star_idx)
            found_numbers.add(number)
        if file[bounds_b][bounds_r].isdigit():
            number = scan_for_number(bottom_row, bounds_r)
            found_numbers.add(number)

        if curr_row[bounds_l].isdigit():
            number = scan_for_number(curr_row, bounds_l)
            found_numbers.add(number)
        if curr_row[bounds_r].isdigit():
            number = scan_for_number(curr_row, bounds_r)
            found_numbers.add(number)

        if len(found_numbers) == 2:
            result.append(functools.reduce(lambda x, y: x * y, found_numbers))

    return sum(result)


def scan_for_number(row: str, index: int):
    found_number = [row[index]]
    left = []
    right = []

    i = 1
    while (index - i) > 0 and row[index - i].isdigit():
        left.append(row[index - i])
        i += 1

    i = 1
    while (index + i) < len(row) and row[index + i].isdigit():
        right.append(row[index + i])
        i += 1

    left.reverse()
    result = int("".join(left + found_number + right))
    return result


def part_01():
    part_number_sum = []
    for idx, _ in enumerate(file):
        part_number_sum.append(get_part_number_sum(idx))

    print("Day 03, Part 1:", sum(part_number_sum))


def part_02():
    gear_sum = []
    for idx, _ in enumerate(file):
        gear_sum.append(get_gear_sum(idx))

    print("Day 03, Part 2:", sum(gear_sum))


if __name__ == "__main__":
    part_01()
    part_02()
    # 79844424
