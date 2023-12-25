from pathlib import Path

file = open(Path(__file__).parent.parent / "inputs/day_13.txt").read()
grids = file.split("\n\n")


def get_diff(lower: str, upper: str) -> int:
    return sum(1 for x, y in zip(upper, lower) if x != y)


def is_reflection(grid, low_bound, upper_bound, smudges=0) -> bool:
    if (
        sum(
            get_diff(lower, upper)
            for lower, upper in zip(reversed(grid[: low_bound + 1]), grid[upper_bound:])
        )
        == smudges
    ):
        return True

    return False


def check_grid(grid, smudges=0) -> int:
    for idx, line in enumerate(grid):
        if idx == 0:
            continue

        if is_reflection(grid, idx - 1, idx, smudges=smudges):
            return idx
    return 0


def part_1():
    result = 0
    for grid in grids:
        grid_split = grid.splitlines()
        result += check_grid(grid_split) * 100

        grid_split = tuple(zip(*grid_split))
        result += check_grid(grid_split)
    print("Day 13, Part 1:", result)


def part_2():
    result = 0
    for grid in grids:
        grid_split = grid.splitlines()
        result += check_grid(grid_split, smudges=1) * 100

        grid_split = tuple(zip(*grid_split))
        result += check_grid(grid_split, smudges=1)
    print("Day 13, Part 2:", result)


if __name__ == "__main__":
    part_1()
    part_2()
