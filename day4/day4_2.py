from typing import Sequence


def is_overlapping(sections_expression_1: str, sections_expression_2: str) -> bool:
    sections_1 = sections_expression_1.split("-")
    start_1 = int(sections_1[0])
    end_1 = int(sections_1[len(sections_1) - 1])

    sections_2 = sections_expression_2.split("-")
    start_2 = int(sections_2[0])
    end_2 = int(sections_2[len(sections_2) - 1])

    return not (end_1 < start_2 or end_2 < start_1)


def get_number_of_overlapping_pairs(lines: Sequence[str]) -> int:
    result = 0

    for line in lines:
        pairs = line.strip().split(",")
        if is_overlapping(pairs[0], pairs[1]):
            result += 1

    return result


def solve() -> None:
    # file = open('sample_input_4.txt', 'r')
    file = open('input_4.txt', 'r')
    lines = file.readlines()
    print(f"Number of overlapping pairs is: {get_number_of_overlapping_pairs(lines)}")


solve()
