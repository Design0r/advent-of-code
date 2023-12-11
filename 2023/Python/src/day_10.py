from pathlib import Path


class Grid:
    def __init__(self, input: list[str]):
        self.directions = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1),
        }
        self.grid = self._parse_input(input)
        self.loop = []
        self.start = self._find_start()
        self.current_pos = self.start
        self.move_history = [self.current_pos]

    def _parse_input(self, input: list[str]) -> list[list[str]]:
        return [list(line) for line in input]

    def _find_start(self) -> tuple[int, int]:
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == "S":
                    return (x, y)
        return (0, 0)

    def find_loop(self) -> None:
        pass

    def move(self, direction: str) -> None:
        y, x = self.directions[direction]
        self.current_pos = (self.current_pos[0] + y, self.current_pos[1] + x)
        self.move_history.append(self.current_pos)

    def print_move_history(self) -> None:
        grid = [["." for _ in range(len(self.grid[0]))] for _ in self.grid]
        for idx, move in enumerate(self.move_history):
            grid[move[0]][move[1]] = str(idx)
        
        print(f"{"="*80}\n\n{"\n".join(["".join(line) for line in grid])}\n")


    def __str__(self) -> str:
        return f"{"="*80}\n\n{"".join(["".join(line) for line in self.grid])}\n"


file = open(Path(__file__).parent.parent / "samples/day_10.txt").readlines()
grid = Grid(file)
grid.move("DOWN")
grid.move("RIGHT")
grid.move("RIGHT")
grid.move("RIGHT")
grid.print_move_history()
