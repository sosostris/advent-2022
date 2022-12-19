from operator import add, sub
from sys import maxsize
from typing import Set, Sequence, Tuple


def build_cubes(lines: Sequence[str]) -> Set[Tuple[int, int, int]]:
    cubes = set()

    for line in lines:
        pos = line.split(",")
        cubes.add((int(pos[0]), int(pos[1]), int(pos[2])))

    return cubes


def get_cube_boundary(cubes: Set[Tuple[int, int, int]]) -> Tuple[Tuple[int, int, int], Tuple[int, int, int]]:
    smallest_x = maxsize
    biggest_x = 0
    smallest_y = maxsize
    biggest_y = 0
    smallest_z = maxsize
    biggest_z = 0

    for cube in cubes:
        smallest_x = min(smallest_x, cube[0])
        biggest_x = max(biggest_x, cube[0])
        smallest_y = min(smallest_y, cube[1])
        biggest_y = max(biggest_y, cube[1])
        smallest_z = min(smallest_z, cube[2])
        biggest_z = max(biggest_z, cube[2])

    return (smallest_x - 1, smallest_y - 1, smallest_z - 1), (biggest_x + 1, biggest_y + 1, biggest_z + 1)


def get_sides(cubes: Set[Tuple[int, int, int]], boundary: Tuple[Tuple[int, int, int], Tuple[int, int, int]]) -> int:
    sides = 0
    visited = set()
    queued = {boundary[0]}
    queue = [boundary[0]]

    while len(queue) > 0:
        current_aired_cell = queue.pop(0)
        visited.add(current_aired_cell)
        queued.remove(current_aired_cell)

        # check up
        if current_aired_cell[1] < boundary[1][1]:
            up_cell = tuple(map(add, current_aired_cell, (0, 1, 0)))
            if up_cell in cubes:
                sides += 1
            elif up_cell not in visited and up_cell not in queued:
                queue.append(up_cell)
                queued.add(up_cell)

        # check down
        if current_aired_cell[1] > boundary[0][1]:
            down_cell = tuple(map(sub, current_aired_cell, (0, 1, 0)))
            if down_cell in cubes:
                sides += 1
            elif down_cell not in visited and down_cell not in queued:
                queue.append(down_cell)
                queued.add(down_cell)

        # check left
        if current_aired_cell[0] > boundary[0][0]:
            left_cell = tuple(map(sub, current_aired_cell, (1, 0, 0)))
            if left_cell in cubes:
                sides += 1
            elif left_cell not in visited and left_cell not in queued:
                queue.append(left_cell)
                queued.add(left_cell)

        # check right
        if current_aired_cell[0] < boundary[1][0]:
            right_cell = tuple(map(add, current_aired_cell, (1, 0, 0)))
            if right_cell in cubes:
                sides += 1
            elif right_cell not in visited and right_cell not in queued:
                queue.append(right_cell)
                queued.add(right_cell)

        # check back
        if current_aired_cell[2] < boundary[1][2]:
            back_cell = tuple(map(add, current_aired_cell, (0, 0, 1)))
            if back_cell in cubes:
                sides += 1
            elif back_cell not in visited and back_cell not in queued:
                queue.append(back_cell)
                queued.add(back_cell)

        # check front
        if current_aired_cell[2] > boundary[0][2]:
            front_cell = tuple(map(sub, current_aired_cell, (0, 0, 1)))
            if front_cell in cubes:
                sides += 1
            elif front_cell not in visited and front_cell not in queued:
                queue.append(front_cell)
                queued.add(front_cell)

    return sides


def solve() -> None:
    # file = open('sample_input_18.txt', 'r')
    file = open('input_18.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    cubes = build_cubes(lines)
    boundary = get_cube_boundary(cubes)
    sides = get_sides(cubes, boundary)

    print(f"Sides of obsidian: {sides}")


solve()
