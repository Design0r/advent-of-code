from pathlib import Path
from utils import IntGrid2D, Vec2

file = open(Path(__file__).parent.parent / "samples/day_17.txt").read().splitlines()
grid = [list(map(int, line)) for line in file]

directions: dict[str, Vec2] = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def move(
    grid: IntGrid2D, pos: Vec2, dir: Vec2, seen: set[Vec2] | None = None, turn_count=0
):
    if not seen:
        seen = {pos}

    py, px = pos
    for k, (dy, dx) in directions.items():
        ny, nx = new_pos = (py + dy, px + dx)
        if new_pos in seen:
            return seen
        if ny < 0 or ny > len(grid) - 1:
            return seen
        elif nx < 0 or nx > len(grid[0]) - 1:
            return seen

        seen = move(grid, new_pos, seen=seen)
