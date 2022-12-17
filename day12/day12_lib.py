from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Pos:
    row: int
    col: int
    steps: int = 0

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))


def build_grid(lines: List[str]) -> List[List[str]]:
    grid = []

    for i in range(0, len(lines)):
        grid.append([])
        for j in range(0, len(lines[i])):
            grid[-1].append(lines[i][j])

    return grid


def get_S_and_E(grid: List[List[str]]) -> Tuple[Pos, Pos]:
    S = Pos(row=0, col=0, steps=0)
    E = Pos(row=0, col=0, steps=0)

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == "S":
                S.row = i
                S.col = j
                grid[i][j] = "a"
            if grid[i][j] == "E":
                E.row = i
                E.col = j
                grid[i][j] = "z"

    return S, E
