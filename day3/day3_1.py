from typing import Sequence, Set
from day3_lib import get_priority_for_item


def get_compartment_common_items(line: str) -> Set[str]:
    sack_items = line.strip()

    compartment_size = int(len(sack_items) / 2)
    compartment_1 = set(sack_items[0:compartment_size])
    compartment_2 = set(sack_items[compartment_size: len(sack_items)])

    return compartment_1 & compartment_2


def get_priorities_sum(lines: Sequence[str]) -> int:
    result = 0

    for line in lines:
        result += sum([get_priority_for_item(item) for item in get_compartment_common_items(line)])

    return result


def solve() -> None:
    # file = open('sample_input_3.txt', 'r')
    file = open('input_3.txt', 'r')
    lines = file.readlines()
    print(f"Sum is: {get_priorities_sum(lines)}")


solve()
