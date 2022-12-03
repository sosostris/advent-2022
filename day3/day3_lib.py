# A -> 65
# Z -> 90
# a -> 97
# z -> 122
def get_priority_for_item(item: str) -> int:
    ascii_code = ord(item)

    if ascii_code <= 90:
        return ascii_code - ord("A") + 27

    return ascii_code - ord("a") + 1
