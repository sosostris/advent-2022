from typing import Sequence
from day10_lib import calc_x_at_cycle_starts, get_instruction


def draw(x_at_cycle_starts: Sequence[int]) -> None:
    for i in range(1, 241):
        x_at_cycle_start = x_at_cycle_starts[i - 1]
        draw_pos = (i - 1) % 40

        if abs(x_at_cycle_start - draw_pos) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if i % 40 == 0:
            print()


def solve() -> None:
    # file = open('sample_input_10.txt', 'r')
    file = open('input_10.txt', 'r')
    instructions = [get_instruction(line) for line in file.readlines()]
    x_at_cycles = calc_x_at_cycle_starts(instructions)
    draw(x_at_cycles)


solve()
