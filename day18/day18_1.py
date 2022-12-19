from typing import Set, Sequence, Tuple


def build_cubes(lines: Sequence[str]) -> Set[Tuple[int, int, int]]:
    cubes = set()

    for line in lines:
        pos = line.split(",")
        cubes.add((int(pos[0]), int(pos[1]), int(pos[2])))

    return cubes


def get_sides(cubes: Set[Tuple[int, int, int]]) -> int:
    sides = 6 * len(cubes)

    for cube in cubes:
        # check up
        up_cube = (cube[0], cube[1] + 1, cube[2])
        if up_cube in cubes:
            sides -= 1

        # check down
        down_cube = (cube[0], cube[1] - 1, cube[2])
        if down_cube in cubes:
            sides -= 1

        # check left
        left_cube = (cube[0] - 1, cube[1], cube[2])
        if left_cube in cubes:
            sides -= 1

        # check right
        right_cube = (cube[0] + 1, cube[1], cube[2])
        if right_cube in cubes:
            sides -= 1

        # check front
        front_cube = (cube[0], cube[1], cube[2] - 1)
        if front_cube in cubes:
            sides -= 1

        # check back
        back_cube = (cube[0], cube[1], cube[2] + 1)
        if back_cube in cubes:
            sides -= 1

    return sides


def solve() -> None:
    # file = open('sample_input_18.txt', 'r')
    file = open('input_18.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    cubes = build_cubes(lines)
    sides = get_sides(cubes)

    print(f"Sides of obsidian: {sides}")


solve()
