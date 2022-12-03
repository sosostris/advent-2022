from typing import Sequence
from day3_lib import get_priority_for_item


def get_priorities_sum_for_badges(lines: Sequence[str]) -> int:
    result = 0

    group_sacks = []

    count = 0
    for line in lines:
        group_sacks.append(set(line.strip()))

        count += 1

        if count == 3:
            badge = group_sacks[0] & group_sacks[1] & group_sacks[2]
            result += get_priority_for_item(list(badge)[0])

            group_sacks.clear()
            count = 0

    return result


def solve() -> None:
    # file = open('sample_input_3.txt', 'r')
    file = open('input_3.txt', 'r')
    lines = file.readlines()
    print(f"Sum is: {get_priorities_sum_for_badges(lines)}")


solve()
