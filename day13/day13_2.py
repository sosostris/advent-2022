from typing import List
from ast import literal_eval
import functools
from day13_lib import are_lists_in_order, compare_lists


def swap(lists: List, pos_1: int, pos_2: int) -> None:
    temp = lists[pos_1]
    lists[pos_1] = lists[pos_2]
    lists[pos_2] = temp


def partition(lists: List, low: int, high: int) -> int:
    pivot = lists[high]
    pivot_index = low

    for i in range(low, high):
        if are_lists_in_order(lists[i], pivot):
            swap(lists, i, pivot_index)
            pivot_index += 1

    swap(lists, pivot_index, high)

    return pivot_index


def quick_sort(lists: List, low: int, high: int) -> None:
    if low >= high:
        return

    pivot_index = partition(lists, low, high)
    quick_sort(lists, low, pivot_index - 1)
    quick_sort(lists, pivot_index + 1, high)


def build_lists(lines: List[str]) -> List:
    lists = [[[2]], [[6]]]
    for line in lines:
        if line == "":
            continue
        lists.append(literal_eval(line))

    return lists


def calc_decode_key(lists: List) -> int:
    decode_key = 1

    for i in range(0, len(lists)):
        if lists[i] == [[2]]:
            decode_key *= i + 1
        if lists[i] == [[6]]:
            decode_key *= i + 1

    return decode_key


def solve() -> None:
    # file = open('sample_input_13.txt', 'r')
    file = open('input_13.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    lists = build_lists(lines)

    sorted_lists = sorted(lists, key=functools.cmp_to_key(compare_lists))
    print(f"Decode key is: {calc_decode_key(sorted_lists)}")

    # quick_sort(lists, 0, len(lists) - 1)
    # print(f"Decode key is: {calc_decode_key(lists)}")


solve()
