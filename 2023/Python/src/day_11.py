from collections import deque
from pathlib import Path


file = open(Path(__file__).parent.parent / "samples/day_11.txt").readlines()


def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        (x, y), depth = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and grid[nx][ny] != "#"
                and (nx, ny) not in seen
            ):
                queue.append(((nx, ny), depth + 1))
                seen.add((nx, ny))
    return seen


# Driver code
start = (0, 4)  # Starting position (for '1')
grid = [list(line.strip()) for line in file]
distances = bfs(grid, start)
print(len(distances) * 2)
