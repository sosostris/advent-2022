from typing import Sequence
from day5_lib import Instruction, get_move_instruction, get_top_items, init_stack


def move(stacks: Sequence[Sequence[str]], instruction: Instruction) -> None:
    times = instruction.times
    from_stack = stacks[instruction.from_stack - 1]
    to_stack = stacks[instruction.to_stack - 1]

    while times > 0:
        item = from_stack.pop()
        to_stack.append(item)

        times -= 1


def solve() -> None:
    stacks = init_stack()

    # file = open('sample_input_5_steps.txt', 'r')
    file = open('input_5_steps.txt', 'r')
    lines = file.readlines()

    for line in lines:
        instruction = get_move_instruction(line.strip())
        move(stacks, instruction)

    print(f"Top items are: {get_top_items(stacks)}")


solve()
