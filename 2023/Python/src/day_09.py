from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_09.txt").readlines()

datasets = [[int(x) for x in line.strip().split(" ")] for line in file]


def traverse_set(dataset: list[int]):
    return_sets = []

    sub_sets = []
    for idx, i in enumerate(dataset):
        if idx < len(dataset) - 1:
            sub_sets.append(dataset[idx + 1] - i)

    return_sets.append(sub_sets)
    if len(s := set(sub_sets)) == 1 and 0 in s:
        return return_sets

    t = traverse_set(sub_sets)
    return_sets.extend(t)

    return return_sets


def part_1():
    result = 0
    for dataset in datasets:
        sets = list(reversed((dataset, *traverse_set(dataset))))

        for idx, i in enumerate(sets):
            if len(s := set(i)) == 1 and 0 in s:
                sets[idx].append(0)
            else:
                next_num = sets[idx - 1][-1] + i[-1]
                sets[idx].append(next_num)

                if idx == len(sets) - 1:
                    result += next_num

    print("Day 09, Part 1:", result)


def part_2():
    result = 0
    for dataset in datasets:
        sets = list(reversed((dataset, *traverse_set(dataset))))

        for idx, i in enumerate(sets):
            if len(s := set(i)) == 1 and 0 in s:
                sets[idx].append(0)
            else:
                next_num = i[0] - sets[idx - 1][0]
                sets[idx].insert(0, next_num)
                if idx == len(sets) - 1:
                    result += next_num
    print("Day 09, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
