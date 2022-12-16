from typing import Mapping, Set
from day14_lib import build_wall


# def get_units_of_resting_sands(wall: Mapping[int, Set], source_x: int, source_y: int) -> int:
#     if source_x not in wall:
#         return 0
#
#     floor = {x: max(ys) for x, ys in wall.items()}
#     units_of_sand = 0
#
#     def will_sand_stop(x: int, y: int) -> bool:
#         while True:
#             # No wall at x at all, the sand goes into abyss
#             if x not in wall:
#                 return False
#
#             # The sand has dropped below floor and goes on into abyss
#             if y > floor[x]:
#                 return False
#
#             while y not in wall[x]:
#                 y += 1
#             # go back one step
#             y = y - 1
#
#             # Check if left diagonal is empty
#             if (x - 1 not in wall) or (x - 1 in wall and y+1 not in wall[x - 1]):
#                 x, y = x - 1, y + 1
#                 continue
#
#             # Check if right diagonal is empty
#             if (x + 1 not in wall) or (x + 1 in wall and y + 1 not in wall[x + 1]):
#                 x, y = x + 1, y + 1
#                 continue
#
#             # The sand has no place to go and stops
#             wall[x].add(y)
#             return True
#
#     while will_sand_stop(source_x, source_y):
#         units_of_sand += 1
#
#     return units_of_sand


def sand_fall(wall: Mapping[int, Set[int]], source_x: int, source_y: int) -> bool:
    floor = {x: max(ys) for x, ys in wall.items()}

    current_x = source_x
    current_y = source_y

    while True:
        if current_x not in wall:
            return False

        if current_y > floor[current_x]:
            return False

        # is blocked
        if (current_x - 1 in wall and current_y + 1 in wall[current_x - 1]) and current_y + 1 in wall[current_x] and (
                current_x + 1 in wall and current_y + 1 in wall[current_x + 1]):
            wall[current_x].add(current_y)
            return True

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


def get_number_of_resting_sands(wall: Mapping[int, Set[int]], source_x: int, source_y: int) -> int:
    count = 0
    while sand_fall(wall, source_x, source_y):
        count += 1

    return count


def solve(source_x, source_y) -> None:
    # file = open('sample_input_14.txt', 'r')
    file = open('input_14.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    wall = build_wall(lines)
    print(f"Number of resting sands: {get_number_of_resting_sands(wall, source_x, source_y)}")


solve(500, 0)
