from typing import Optional, List


def are_lists_in_order(list_1: List, list_2: List) -> Optional[bool]:
    if len(list_1) == 0 and len(list_2) == 0:
        return None

    if len(list_1) == 0 and len(list_2) > 0:
        return True

    if len(list_1) > 0 and len(list_2) == 0:
        return False

    next_element_1 = list_1[0]
    next_element_2 = list_2[0]

    # both next elements are integer
    if isinstance(next_element_1, int) and isinstance(next_element_2, int):
        if next_element_1 > next_element_2:
            return False
        elif next_element_1 < next_element_2:
            return True
        else:
            return are_lists_in_order(list_1[1:], list_2[1:])

    # list_1 next element is int, list_2 next element is list
    elif isinstance(next_element_1, int):
        list_1[0] = [list_1[0]]
        in_order = are_lists_in_order(list_1, list_2)
        list_1[0] = list_1[0][0]
        return in_order

    # list_2 next element is int, list_1 next element is list
    elif isinstance(next_element_2, int):
        list_2[0] = [list_2[0]]
        in_order = are_lists_in_order(list_1, list_2)
        list_2[0] = list_2[0][0]
        return in_order

    # both next element of list_1 and list_2 are list
    else:
        next_in_order = are_lists_in_order(next_element_1, next_element_2)
        if next_in_order is None:
            return are_lists_in_order(list_1[1:], list_2[1:])
        return next_in_order


def compare_lists(list_1: List, list_2: List) -> int:
    if len(list_1) == 0 and len(list_2) == 0:
        return 0

    if len(list_1) == 0 and len(list_2) > 0:
        return -1

    if len(list_1) > 0 and len(list_2) == 0:
        return 1

    next_element_1 = list_1[0]
    next_element_2 = list_2[0]

    # both next elements are integer
    if isinstance(next_element_1, int) and isinstance(next_element_2, int):
        if next_element_1 > next_element_2:
            return 1
        elif next_element_1 < next_element_2:
            return -1
        else:
            return compare_lists(list_1[1:], list_2[1:])

    # list_1 next element is int, list_2 next element is list
    elif isinstance(next_element_1, int):
        list_1[0] = [list_1[0]]
        in_order = compare_lists(list_1, list_2)
        list_1[0] = list_1[0][0]
        return in_order

    # list_2 next element is int, list_1 next element is list
    elif isinstance(next_element_2, int):
        list_2[0] = [list_2[0]]
        in_order = compare_lists(list_1, list_2)
        list_2[0] = list_2[0][0]
        return in_order

    # both next element of list_1 and list_2 are list
    else:
        next_in_order = compare_lists(next_element_1, next_element_2)
        if next_in_order == 0:
            return compare_lists(list_1[1:], list_2[1:])
        return next_in_order
