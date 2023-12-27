from pathlib import Path
import sys
from utils import timeit
sys.setrecursionlimit(1000000000)

file = open(Path(__file__).parent.parent / "samples/day_10.txt").readlines()

class Grid:
    def __init__(self, input: list[str]):
        self.directions = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1),
        }
        self.possible_symbols = {"UP": ("|",  "7", "F", "S"), "DOWN": ("|", "L", "J", "S"), "LEFT": ("-", "L", "F", "S"), "RIGHT": ("-", "7", "J", "S")}
        self.possible_dirs = {"|":("UP", "DOWN"),"-": ("LEFT", "RIGHT"), "L": ("UP", "RIGHT"), "J": ("UP", "LEFT"), "F": ("DOWN", "RIGHT"), "7": ("DOWN", "LEFT")}
        self.grid = self._parse_input(input)
        self.start = self._find_start()
        self.move_history = {0: self.start}

    def _parse_input(self, input: list[str]) -> list[list[str]]:
        return [list(line.strip()) for line in input]

    def _find_start(self) -> tuple[int, int]:
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == "S":
                    return (y, x)
        return (0, 0)

    def find_loop(self) -> None:
        pass
    
    def is_possible_move(self, direction: str, current: tuple[int, int], next: tuple[int, int]) -> bool:
        n_y,n_x = next
        c_y,c_x = current
        if 0 <= n_y < len(self.grid) and 0 <= n_x < len(self.grid[0]):
            possible_symbols = self.possible_symbols[direction]
            next_symbol = self.grid[n_y][n_x]
            curr_symbol = self.grid[c_y][c_x]
            if next_symbol in possible_symbols and direction in self.possible_dirs.get(curr_symbol, ("UP", "DOWN", "LEFT", "RIGHT")):
                return True
            return False
        
        return False
        
    def move(self, direction: str, current_pos: tuple[int, int]) -> tuple[int, int]:
        y, x = self.directions[direction]
        current_pos = (current_pos[0] + y, current_pos[1] + x)
        return current_pos

    def print_move_history(self) -> None:
        grid = [["." for _ in range(len(self.grid[0]))] for _ in self.grid]
        for idx, (i, move) in enumerate(self.move_history.items()):
            grid[move[0]][move[1]] = str(idx)
        
        print(f"{"="*80}\n\n{"\n".join(["  ".join(line) for line in grid])}\n")

    def get_next_move(self, current_pos, visited=None):
        if visited is None:
            visited = set()
        visited.add(current_pos)
        #grid.print_move_history()

        if current_pos == self.start and len(visited) > 1:
            return

        for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            new_pos = self.move(direction, current_pos)

            if new_pos not in visited and self.is_possible_move(direction, current_pos, new_pos):
                self.move_history[len(visited )] = new_pos
                self.get_next_move(new_pos, visited)

        return

    def get_enclosed(self) -> int:
        counter = 0
        num_of_collisios = 0
        grid = [["." for _ in range(len(self.grid[0]))] for _ in self.grid]
        for idx, (i, move) in enumerate(self.move_history.items()):
            grid[move[0]][move[1]] = str(idx)

        for y_idx, line in enumerate(grid):
            for x_idx, char in enumerate(line):
                if char.isdigit():
                    num_of_collisios += 1
                else:
                    if num_of_collisios % 2 != 0:
                        counter += 1
        return counter
                    
      
    def __str__(self) -> str:
        return f"{"="*80}\n\n{"".join(["".join(line) for line in self.grid])}\n"



def main():
    grid = Grid(file)
    grid.get_next_move(grid.start)
    print("Day 10, Part 1:", len(grid.move_history)//2)
    grid.get_next_move(grid.start)
    grid.print_move_history()
    print("Day 10, Part 2:", grid.get_enclosed())


if __name__ == "__main__":
    main()
