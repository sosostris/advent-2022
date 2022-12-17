from typing import List
from ast import literal_eval
from day13_lib import are_lists_in_order


def get_sum_of_pairs_in_right_order(lines: List[str]) -> int:
    pair_index_sum = 0

    for i in range(0, len(lines) - 2, 3):
        list_1 = literal_eval(lines[i])
        list_2 = literal_eval(lines[i + 1])

        if are_lists_in_order(list_1, list_2):
            pair_index_sum += int(i / 3) + 1

    return pair_index_sum


def solve() -> None:
    # file = open('sample_input_13.txt', 'r')
    file = open('input_13.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    pair_index_sum = get_sum_of_pairs_in_right_order(lines)
    print(f"Sum of pair index in right order is: {pair_index_sum}")


solve()
