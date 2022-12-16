from typing import Mapping, Set
from day14_lib import build_wall


def get_ground(wall: Mapping[int, Set[int]]) -> int:
    floor = {x: max(ys) for x, ys in wall.items()}

    max_y = 0
    for x in floor:
        current_max_y = floor[x]
        if current_max_y > max_y:
            max_y = current_max_y

    ground = max_y + 2

    return ground


def sand_fall(wall: Mapping[int, Set[int]], source_x: int, source_y: int, ground: int) -> None:
    current_x = source_x
    current_y = source_y

    while True:
        # is blocked
        if is_blocked(wall, current_x, current_y, ground):
            wall[current_x].add(current_y)
            break

        # slide down
        if current_y + 1 not in wall[current_x]:
            current_y += 1
            continue

        # slide left down
        if current_x - 1 not in wall or current_y + 1 not in wall[current_x - 1]:
            current_y += 1
            current_x -= 1
            continue

        # slide right down
        if current_x + 1 not in wall or current_y + 1 not in wall[current_x + 1]:
            current_y += 1
            current_x += 1
            continue


def is_blocked(wall: Mapping[int, Set[int]], x: int, y: int, ground: int) -> bool:
    if y + 1 == ground:
        return True

    is_left_down_blocked = x - 1 in wall and y + 1 in wall[x - 1]
    is_down_blocked = x in wall and y + 1 in wall[x]
    is_right_down_blocked = x + 1 in wall and y + 1 in wall[x + 1]

    return is_left_down_blocked and is_down_blocked and is_right_down_blocked


def get_number_of_resting_sands(wall: Mapping[int, Set[int]], source_x: int, source_y: int, ground: int) -> int:
    count = 0
    while True:
        sand_fall(wall, source_x, source_y, ground)
        count += 1
        if is_blocked(wall, source_x, source_y, ground):
            break

    return count + 1


def solve(source_x, source_y) -> None:
    # file = open('sample_input_14.txt', 'r')
    file = open('input_14.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    wall = build_wall(lines)
    ground = get_ground(wall)
    print(f"Number of resting sands: {get_number_of_resting_sands(wall, source_x, source_y, ground)}")


solve(500, 0)
