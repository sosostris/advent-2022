from typing import List, Tuple
from day17_lib import RockPos, create_rock, get_height_of_rock_tower, init_cave


def get_first_two_occurrences_of_repeating_pattern(cave: List[List[int]],
                                                   jet_pattern: str,
                                                   rocks: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    jet_pattern_pos = 0
    current_top = -1

    first_match = False
    second_match = False

    first_rock = (0, 0)
    second_rock = (0, 0)

    for i in range(0, rocks):
        rock_index = i % 5
        rock_pos = RockPos(2, current_top + 4)
        rock = create_rock(rock_index, rock_pos)

        can_fall = True

        while can_fall:
            jet_pattern_pos = jet_pattern_pos % len(jet_pattern)
            jet_direction = jet_pattern[jet_pattern_pos]
            jet_pattern_pos += 1
            if jet_direction == "<":
                rock.move_left(cave)
            elif jet_direction == ">":
                rock.move_right(cave)

            if not rock.move_down(cave):
                can_fall = False

        rock.add_rock_to_cave(cave)
        current_top = max(current_top, rock.pos.y + rock.height - 1)

        if is_out_line_repeating(cave[current_top - 9:current_top + 1], jet_pattern_pos, rock_index):
            if not first_match:
                print(f"Found first occurrence pattern at rock {i + 1}, current height is {current_top + 1}")
                first_match = True
                first_rock = (i + 1, current_top + 1)
            elif not second_match:
                print(f"Found second occurrence at rock {i + 1}, current height is {current_top + 1}")
                second_match = True
                second_rock = (i + 1, current_top + 1)
                return first_rock, second_rock

        while len(cave) <= current_top + 7:
            cave.append([0, 0, 0, 0, 0, 0, 0])


def is_out_line_repeating(top_10_rows: List[List[int]], jet_pattern: int, rock_index: int) -> bool:
    """
    check if it is a repeating pattern:
      1) current rock index is 1
      2) next jet pattern pos is 7518
      3) the contour of top rocks after current rock settles is as follows:
        .....#.
        ....###
        .....#.
        ..####.
        ....#..
        ....#..
        ....#..
        ....#..
        ###.#..
        ######.
    """
    if jet_pattern != 7518 or rock_index != 1:
        return False

    if (top_10_rows[9] == [0, 0, 0, 0, 0, 1, 0] and
            top_10_rows[8] == [0, 0, 0, 0, 1, 1, 1] and
            top_10_rows[7][:6] == [0, 0, 0, 0, 0, 1] and
            top_10_rows[6][:5] == [0, 0, 1, 1, 1] and
            top_10_rows[5][:5] == [0, 0, 0, 0, 1] and
            top_10_rows[4][:5] == [0, 0, 0, 0, 1] and
            top_10_rows[3][:5] == [0, 0, 0, 0, 1] and
            top_10_rows[2][:5] == [0, 0, 0, 0, 1] and
            top_10_rows[1][:5] == [1, 1, 1, 0, 1] and
            top_10_rows[0][3] == 1):
        return True

    return False


def solve(rocks: int) -> None:
    # file = open('sample_input_17.txt', 'r')
    file = open('input_17.txt', 'r')
    jet_pattern = [line.strip() for line in file.readlines()][0]
    cave = init_cave()

    # judging from the fact that the input is extremely large,
    # it is highly likely there will be repeating patterns of the rock falls
    # a repeating pattern is defined as:
    #   1) next rock is same rock
    #   2) next jet flow is same
    #   3) top rows contour is the same (forming a logical "floor" although it could be unflat

    # we think if we run 10000 rocks most likely a recurring pattern already occurred
    # we therefore run day17_1.py with 10000 as input and find a candidate repeating pattern
    #   1) current rock index is 1
    #   2) next jet instruction position is 7518
    #   3) top contour is as shown in method is_out_line_repeating
    # then we get the first and second occurrences of the contour

    # with cycle length and cycle height we can mathematically calculate the final rock tower height

    first_rock, second_rock = get_first_two_occurrences_of_repeating_pattern(cave, jet_pattern, rocks)
    cycle_length = second_rock[0] - first_rock[0]
    cycles = (rocks - first_rock[0]) // cycle_length
    cycle_height = second_rock[1] - first_rock[1]
    remaining_rocks = (rocks - first_rock[0]) % cycle_length
    
    height = cycles * cycle_height + get_height_of_rock_tower(init_cave(), jet_pattern, first_rock[0] + remaining_rocks)
    print(f"Rock height after {rocks} rock falls: {height}")


solve(1000000000000)
