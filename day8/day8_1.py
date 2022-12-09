from typing import Sequence
from dataclasses import dataclass


@dataclass
class TreeView:
    blocking_pos: int
    highest: int


@dataclass
class DirectionalTreeView:
    up: TreeView
    down: TreeView
    left: TreeView
    right: TreeView


def init_tree_grid(rows: Sequence[str]) -> Sequence[Sequence[int]]:
    tree_grid = []

    for row in rows:
        tree_row = []
        row = row.strip()
        for height in row:
            tree_row.append(int(height))
        tree_grid.append(tree_row)

    return tree_grid


def is_visible(height: int, surrounding_heights: DirectionalTreeView) -> bool:
    return height > surrounding_heights.up.highest \
           or height > surrounding_heights.down.highest \
           or height > surrounding_heights.left.highest \
           or height > surrounding_heights.right.highest


def get_blocking_pos_up(tree_grid: Sequence[Sequence[int]], max_height_grid: Sequence[Sequence[DirectionalTreeView]], i: int, j: int) -> int:
    up_tree = max_height_grid[i - 1][j]

    while up_tree.up.blocking_pos >= 0:
        if tree_grid[up_tree.up.blocking_pos][j] >= tree_grid[i][j]:
            return up_tree.up.blocking_pos
        up_tree = max_height_grid[up_tree.up.blocking_pos][j]

    return -1


def get_blocking_pos_down(tree_grid: Sequence[Sequence[int]], max_height_grid: Sequence[Sequence[DirectionalTreeView]], i: int, j: int) -> int:
    down_tree = max_height_grid[i + 1][j]

    while down_tree.down.blocking_pos >= 0:
        if tree_grid[down_tree.down.blocking_pos][j] >= tree_grid[i][j]:
            return down_tree.down.blocking_pos
        down_tree = max_height_grid[down_tree.down.blocking_pos][j]

    return -1


def get_blocking_pos_left(tree_grid: Sequence[Sequence[int]], max_height_grid: Sequence[Sequence[DirectionalTreeView]], i: int, j: int) -> int:
    left_tree = max_height_grid[i][j - 1]

    while left_tree.left.blocking_pos >= 0:
        if tree_grid[i][left_tree.left.blocking_pos] >= tree_grid[i][j]:
            return left_tree.left.blocking_pos
        left_tree = max_height_grid[i][left_tree.left.blocking_pos]

    return -1


def get_blocking_pos_right(tree_grid: Sequence[Sequence[int]], max_height_grid: Sequence[Sequence[DirectionalTreeView]], i: int, j: int) -> int:
    right_tree = max_height_grid[i][j + 1]

    while right_tree.right.blocking_pos >= 0:
        if tree_grid[i][right_tree.right.blocking_pos] >= tree_grid[i][j]:
            return right_tree.right.blocking_pos
        right_tree = max_height_grid[i][right_tree.right.blocking_pos]

    return -1


def get_directional_tree_views(tree_grid: Sequence[Sequence[int]]) -> Sequence[Sequence[DirectionalTreeView]]:
    direction_tree_view_grid = []

    for i in range(len(tree_grid)):
        direction_tree_view_grid.append([])

    for i in range(len(tree_grid)):
        for j in range(len(tree_grid[i])):
            left = TreeView(blocking_pos=-1, highest=0)
            right = TreeView(blocking_pos=-1, highest=0)
            up = TreeView(blocking_pos=-1, highest=0)
            down = TreeView(blocking_pos=-1, highest=0)
            direction_tree_view_grid[i].append(DirectionalTreeView(left=left, right=right, up=up, down=down))

            if j > 0:
                if tree_grid[i][j] <= tree_grid[i][j - 1]:
                    direction_tree_view_grid[i][j].left.blocking_pos = j - 1
                else:
                    blocking_pos = get_blocking_pos_left(tree_grid, direction_tree_view_grid, i, j)
                    direction_tree_view_grid[i][j].left.blocking_pos = blocking_pos

                direction_tree_view_grid[i][j].left.highest = max(direction_tree_view_grid[i][j - 1].left.highest, tree_grid[i][j - 1])

    for i in range(len(tree_grid)):
        for j in range(len(tree_grid[i]) - 1, -1, -1):
            if j < len(tree_grid[i]) - 1:
                if tree_grid[i][j] <= tree_grid[i][j + 1]:
                    direction_tree_view_grid[i][j].right.blocking_pos = j + 1
                else:
                    blocking_pos = get_blocking_pos_right(tree_grid, direction_tree_view_grid, i, j)
                    direction_tree_view_grid[i][j].right.blocking_pos = blocking_pos

                direction_tree_view_grid[i][j].right.highest = max(direction_tree_view_grid[i][j + 1].right.highest, tree_grid[i][j + 1])

    for i in range(len(tree_grid)):
        for j in range(len(tree_grid[i])):
            if i > 0:
                if tree_grid[i][j] <= tree_grid[i - 1][j]:
                    direction_tree_view_grid[i][j].up.blocking_pos = i - 1
                else:
                    blocking_pos = get_blocking_pos_up(tree_grid, direction_tree_view_grid, i, j)
                    direction_tree_view_grid[i][j].up.blocking_pos = blocking_pos
                direction_tree_view_grid[i][j].up.highest = max(direction_tree_view_grid[i - 1][j].up.highest, tree_grid[i - 1][j])

    for i in range(len(tree_grid) - 1, -1, -1):
        for j in range(len(tree_grid[i])):
            if i < len(tree_grid) - 1:
                if tree_grid[i][j] <= tree_grid[i + 1][j]:
                    direction_tree_view_grid[i][j].down.blocking_pos = i + 1
                else:
                    blocking_pos = get_blocking_pos_down(tree_grid, direction_tree_view_grid, i, j)
                    direction_tree_view_grid[i][j].down.blocking_pos = blocking_pos
                direction_tree_view_grid[i][j].down.highest = max(direction_tree_view_grid[i + 1][j].down.highest, tree_grid[i + 1][j])

    return direction_tree_view_grid


def get_number_of_visible_trees(tree_grid: Sequence[Sequence[int]],
                                max_height_grid: Sequence[Sequence[DirectionalTreeView]]) -> int:
    count = 0

    for i in range(1, len(max_height_grid) - 1):
        for j in range(1, len(max_height_grid[i]) - 1):
            if is_visible(tree_grid[i][j], max_height_grid[i][j]):
                count += 1

    number_of_outer_trees = len(tree_grid) * 2 + (len(tree_grid[0]) - 2) * 2

    return count + number_of_outer_trees


def get_highest_scenic_score(tree_grid: Sequence[Sequence[int]], max_height_grid: Sequence[Sequence[DirectionalTreeView]]) -> int:
    max_scenic_score = 0

    for i in range(1, len(max_height_grid) - 1):
        for j in range(1, len(max_height_grid[i]) - 1):
            scenic_score = 1

            if max_height_grid[i][j].left.blocking_pos == -1:
                view_distance_left = j
            else:
                view_distance_left = j - max_height_grid[i][j].left.blocking_pos
            scenic_score *= view_distance_left

            if max_height_grid[i][j].right.blocking_pos == -1:
                view_distance_right = len(tree_grid[i]) - j - 1
            else:
                view_distance_right = max_height_grid[i][j].right.blocking_pos - j
            scenic_score *= view_distance_right

            if max_height_grid[i][j].up.blocking_pos == -1:
                view_distance_up = i
            else:
                view_distance_up = i - max_height_grid[i][j].up.blocking_pos
            scenic_score *= view_distance_up

            if max_height_grid[i][j].down.blocking_pos == -1:
                view_distance_down = len(tree_grid) - i - 1
            else:
                view_distance_down = max_height_grid[i][j].down.blocking_pos - i
            scenic_score *= view_distance_down

            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


def solve() -> None:
    # file = open('sample_input_8.txt', 'r')
    file = open('input_8.txt', 'r')
    lines = file.readlines()

    tree_grid = init_tree_grid(lines)
    directional_tree_view_grid = get_directional_tree_views(tree_grid)
    number_of_visible_trees = get_number_of_visible_trees(tree_grid, directional_tree_view_grid)

    print(f"Number of visible trees: {number_of_visible_trees}")
    print(f"Max scenic score: {get_highest_scenic_score(tree_grid, directional_tree_view_grid)}")


solve()
