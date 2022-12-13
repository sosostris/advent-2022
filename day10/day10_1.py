from typing import Sequence
from day10_lib import calc_x_at_cycle_starts, get_instruction


def calc_signal_strengths_at_cycles(cycles: Sequence[int], x_at_cycles: Sequence[int]) -> int:
    result = 0
    for cycle in cycles:
        result += x_at_cycles[cycle - 1] * cycle

    return result


def solve(cycles: Sequence[int]) -> None:
    # file = open('sample_input_10.txt', 'r')
    file = open('input_10.txt', 'r')
    instructions = [get_instruction(line) for line in file.readlines()]
    x_at_cycles = calc_x_at_cycle_starts(instructions)
    print(f"Sum of signal strengths: {calc_signal_strengths_at_cycles(cycles, x_at_cycles)}")


solve([20, 60, 100, 140, 180, 220])
