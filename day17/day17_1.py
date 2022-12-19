from day17_lib import get_height_of_rock_tower, init_cave


def solve(rocks: int) -> None:
    #  file = open('sample_input_17.txt', 'r')
    file = open('input_17.txt', 'r')
    jet_pattern = [line.strip() for line in file.readlines()][0]
    cave = init_cave()

    height = get_height_of_rock_tower(cave, jet_pattern, rocks)
    print(f"Rock tower height: {height}")


solve(2022)
