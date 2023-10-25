import time
from typing import List


def importCalories(file: str) -> List[List[int]]:
    all_elf_calories = []
    elf_calories = []

    with open(file) as file:
        for line in file:
            line = line[:-1]

            if line != "":
                elf_calories.append(int(line))

            else:
                all_elf_calories.append(elf_calories)
                elf_calories = []

        # add last entry
        all_elf_calories.append(elf_calories)

    return all_elf_calories


def getMostCalorieElf(elf_list: List[List[int]], elf_num: int) -> int:
    calorie_list = []

    for elf in elf_list:
        calories = 0
        for food in elf:
            calories += food

        calorie_list.append(calories)

    calorie_list.sort(reverse=True)
    calorie_sum = sum(calorie_list[:elf_num])

    return calorie_sum


if __name__ == "__main__":
    start = time.time()
    print(
        getMostCalorieElf(importCalories("day_01/input.txt"), 3),
        f"executed in {time.time() - start}s",
    )
