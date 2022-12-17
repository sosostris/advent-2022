from dataclasses import dataclass, field
from typing import Callable, List


@dataclass
class Monkey:
    items: List[int]
    operation: Callable[[int], int]
    test: Callable[[int], int]
    inspection_times: int = field(default=0, init=False)


def get_test(divisor: int, divisible_next_monkey: int, undivisible_next_monkey: int) -> Callable[[int], int]:
    def test(worry: int) -> int:
        if worry % divisor == 0:
            return divisible_next_monkey

        return undivisible_next_monkey

    return test

