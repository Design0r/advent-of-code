from pathlib import Path
from utils import StrGrid2D, Vec2, timeit

file = open(Path(__file__).parent.parent / "inputs/day_18.txt").read().splitlines()


class DynGrid2D:
    def __init__(self, default_fill: str) -> None:
        self.default_fill = default_fill
        self.grid: StrGrid2D = [[self.default_fill]]

    @property
    def width(self) -> int:
        return len(self.grid[0])

    @property
    def height(self) -> int:
        return len(self.grid)

    def insert(self, value: str, pos: Vec2):
        y, x = pos
        width = self.width - 1
        height = self.height - 1
        if y > height:
            for _ in range(y - height):
                self._add_row()

        if x > width:
            for _ in range(x - width):
                self._add_col()

        self.grid[y][x] = value

    def _add_row(self) -> None:
        self.grid.append([self.default_fill for _ in self.grid[0]])

    def _add_col(self) -> None:
        for g in self.grid:
            g.append(self.default_fill)

    def print(self) -> None:
        print("-" * 40)
        for g in self.grid:
            print("".join(g))

    def fill(self):
        for y_idx, y in enumerate(self.grid):
            intersect = 0
            for x_idx, x in enumerate(y):
                if x == "#":
                    if x_idx + 1 < len(y):
                        if y[x_idx + 1] == ".":
                            intersect += 1

                elif x == "." and intersect % 2 != 0:
                    self.grid[y_idx][x_idx] = "#"


directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}


@timeit
def part_1():
    grid = DynGrid2D(".")
    pos = (100, 100)
    for line in file:
        dir, val, *_ = line.split(" ")
        val = int(val)
        for _ in range(val):
            py, px = pos
            dy, dx = directions[dir]
            pos = (py + dy, px + dx)
            grid.insert("#", pos)

    grid.print()
    grid.fill()
    grid.print()
    print(sum(1 for row in grid.grid for pos in row if pos == "#"))


if __name__ == "__main__":
    part_1()
