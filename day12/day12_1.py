from typing import List
from day12_lib import Pos, build_grid, get_S_and_E


# def get_steps_with_route(S: Pos, E: Pos, grid: List[List[str]]) -> int:
#     queue = []
#     visited = set()
#     in_queue = set()
#     queue.append(S)
#     in_queue.add(S)
#
#     parent: List[List[str]] = []
#     route: List[List[str]] = []
#     for row in grid:
#         parent.append(["." for char in row])
#         route.append(["." for char in row])
#
#     while len(queue) > 0:
#         pos = queue.pop(0)
#         visited.add(pos)
#         in_queue.remove(pos)
#
#         if pos == E:
#             p = E
#             while p != S:
#                 print(p)
#                 if parent[p.row][p.col] == "^":
#                     route[p.row-1][p.col] = "v"
#                     p = Pos(row=p.row-1, col=p.col)
#                     continue
#                 if parent[p.row][p.col] == "v":
#                     route[p.row+1][p.col] = "^"
#                     p = Pos(row=p.row+1, col=p.col)
#                     continue
#                 if parent[p.row][p.col] == "<":
#                     route[p.row][p.col-1] = ">"
#                     p = Pos(row=p.row, col=p.col-1)
#                     continue
#                 if parent[p.row][p.col] == ">":
#                     route[p.row][p.col+1] = "<"
#                     p = Pos(row=p.row, col=p.col+1)
#                     continue
#
#             for line in route:
#                 print(''.join(line))
#             return pos.steps
#
#         current_height = ord(grid[pos.row][pos.col])
#         if pos.row > 0:
#             up_height = ord(grid[pos.row - 1][pos.col])
#             if up_height - current_height <= 1:
#                 up_pos = Pos(row=pos.row - 1, col=pos.col, steps=pos.steps + 1)
#                 if (up_pos not in visited) and (up_pos not in in_queue):
#                     queue.append(up_pos)
#                     in_queue.add(up_pos)
#                     parent[up_pos.row][up_pos.col] = "v"
#
#         if pos.row < len(grid) - 1:
#             down_height = ord(grid[pos.row + 1][pos.col])
#             if down_height - current_height <= 1:
#                 down_pos = Pos(row=pos.row + 1, col=pos.col, steps=pos.steps + 1)
#                 if (down_pos not in visited) and (down_pos not in in_queue):
#                     queue.append(down_pos)
#                     in_queue.add(down_pos)
#                     parent[down_pos.row][down_pos.col] = "^"
#
#         if pos.col > 0:
#             left_height = ord(grid[pos.row][pos.col - 1])
#             if left_height - current_height <= 1:
#                 left_pos = Pos(row=pos.row, col=pos.col - 1, steps=pos.steps + 1)
#                 if (left_pos not in visited) and (left_pos not in in_queue):
#                     queue.append(left_pos)
#                     in_queue.add(left_pos)
#                     parent[left_pos.row][left_pos.col] = ">"
#
#         if pos.col < len(grid[0]) - 1:
#             right_height = ord(grid[pos.row][pos.col + 1])
#             if right_height - current_height <= 1:
#                 right_pos = Pos(row=pos.row, col=pos.col + 1, steps=pos.steps + 1)
#                 if (right_pos not in visited) and (right_pos not in in_queue):
#                     queue.append(right_pos)
#                     in_queue.add(right_pos)
#                     parent[right_pos.row][right_pos.col] = "<"
#
#     return 0


def get_steps(S: Pos, E: Pos, grid: List[List[str]]) -> int:
    queue = []
    visited = set()
    in_queue = set()
    queue.append(S)
    in_queue.add(S)

    while len(queue) > 0:
        pos = queue.pop(0)
        visited.add(pos)
        in_queue.remove(pos)

        if pos == E:
            return pos.steps

        current_height = ord(grid[pos.row][pos.col])
        if pos.row > 0 and ord(grid[pos.row - 1][pos.col]) - current_height <= 1:
            up_pos = Pos(row=pos.row - 1, col=pos.col, steps=pos.steps + 1)
            if (up_pos not in visited) and (up_pos not in in_queue):
                queue.append(up_pos)
                in_queue.add(up_pos)

        if pos.row < len(grid) - 1 and ord(grid[pos.row + 1][pos.col]) - current_height <= 1:
            down_pos = Pos(row=pos.row + 1, col=pos.col, steps=pos.steps + 1)
            if (down_pos not in visited) and (down_pos not in in_queue):
                queue.append(down_pos)
                in_queue.add(down_pos)

        if pos.col > 0 and ord(grid[pos.row][pos.col - 1]) - current_height <= 1:
            left_pos = Pos(row=pos.row, col=pos.col - 1, steps=pos.steps + 1)
            if (left_pos not in visited) and (left_pos not in in_queue):
                queue.append(left_pos)
                in_queue.add(left_pos)

        if pos.col < len(grid[0]) - 1 and ord(grid[pos.row][pos.col + 1]) - current_height <= 1:
            right_pos = Pos(row=pos.row, col=pos.col + 1, steps=pos.steps + 1)
            if (right_pos not in visited) and (right_pos not in in_queue):
                queue.append(right_pos)
                in_queue.add(right_pos)

    return 0


def solve() -> None:
    # file = open('sample_input_12.txt', 'r')
    file = open('input_12.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    grid = build_grid(lines)
    S, E = get_S_and_E(grid)

    print(f"Number of steps: {get_steps(S, E, grid)}")


solve()
