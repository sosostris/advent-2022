from typing import Sequence
from day5_lib import Instruction, get_move_instruction, get_top_items, init_stack


def power_move(stacks: Sequence[Sequence[str]], instruction: Instruction) -> None:
    times = instruction.times
    from_stack = stacks[instruction.from_stack - 1]
    to_stack = stacks[instruction.to_stack - 1]

    moved_stack = from_stack[len(from_stack) - times: len(from_stack)]
    stacks[instruction.from_stack - 1] = from_stack[:len(from_stack) - times]
    to_stack.extend(moved_stack)


def solve() -> None:
    stacks = init_stack()

    # file = open('sample_input_5_steps.txt', 'r')
    file = open('input_5_steps.txt', 'r')
    lines = file.readlines()

    for line in lines:
        instruction = get_move_instruction(line.strip())
        power_move(stacks, instruction)

    print(f"Top items are: {get_top_items(stacks)}")


solve()
