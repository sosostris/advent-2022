from sys import maxsize
from typing import List
from day12_lib import Pos, build_grid, get_S_and_E


def get_distances(E: Pos, grid: List[List[str]]) -> List[List[int]]:
    distances = []
    for row in grid:
        distances.append([])
        for col in row:
            distances[-1].append(maxsize)

    queue = []
    visited = set()
    in_queue = set()
    queue.append(E)
    in_queue.add(E)

    while len(queue) > 0:
        pos = queue.pop(0)
        distances[pos.row][pos.col] = pos.steps
        visited.add(pos)
        in_queue.remove(pos)

        current_height = ord(grid[pos.row][pos.col])
        if pos.row > 0 and ord(grid[pos.row - 1][pos.col]) - current_height >= -1:
            up_pos = Pos(row=pos.row - 1, col=pos.col, steps=pos.steps + 1)
            if (up_pos not in visited) and (up_pos not in in_queue):
                queue.append(up_pos)
                in_queue.add(up_pos)

        if pos.row < len(grid) - 1 and ord(grid[pos.row + 1][pos.col]) - current_height >= -1:
            down_pos = Pos(row=pos.row + 1, col=pos.col, steps=pos.steps + 1)
            if (down_pos not in visited) and (down_pos not in in_queue):
                queue.append(down_pos)
                in_queue.add(down_pos)

        if pos.col > 0 and ord(grid[pos.row][pos.col - 1]) - current_height >= -1:
            left_pos = Pos(row=pos.row, col=pos.col - 1, steps=pos.steps + 1)
            if (left_pos not in visited) and (left_pos not in in_queue):
                queue.append(left_pos)
                in_queue.add(left_pos)

        if pos.col < len(grid[0]) - 1 and ord(grid[pos.row][pos.col + 1]) - current_height >= -1:
            right_pos = Pos(row=pos.row, col=pos.col + 1, steps=pos.steps + 1)
            if (right_pos not in visited) and (right_pos not in in_queue):
                queue.append(right_pos)
                in_queue.add(right_pos)

    return distances


def get_shortest_path(grid: List[List[str]], distances: List[List[int]]) -> int:
    shortest_path = maxsize

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "a" and distances[i][j] < shortest_path:
                shortest_path = distances[i][j]

    return shortest_path


def solve() -> None:
    # file = open('sample_input_12.txt', 'r')
    file = open('input_12.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    grid = build_grid(lines)
    S, E = get_S_and_E(grid)
    distances = get_distances(E, grid)
    shortest_path = get_shortest_path(grid, distances)

    print(f"Shortest path steps: {shortest_path}")


solve()
