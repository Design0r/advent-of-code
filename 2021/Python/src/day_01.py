from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_01.txt").read().splitlines()


def day_01():
    result = sum(1 for curr, prev in zip(file[1:], file) if int(curr) > int(prev))
    print("Day 01, Part 1:", result)


def sliding_window(iterable: list, num: int):
    slices = (iterable[i:] for i in range(num))
    for window in zip(*slices):
        yield window


def day_02():
    nums = [int(i) for i in file]
    result = sum(
        1
        for curr, prev in zip(sliding_window(nums[1:], 3), sliding_window(nums, 3))
        if sum(curr) > sum(prev)
    )
    print("Day 01, Part 2:", result)


if __name__ == "__main__":
    day_01()
    day_02()
