from dataclasses import dataclass
from typing import Sequence
from re import search


@dataclass
class Instruction:
    times: int
    from_stack: int
    to_stack: int


def init_stack() -> Sequence[Sequence[str]]:
    stacks = []
    current_stack = []

    file = open('input_5_init_stacks.txt', 'r')
    lines = file.readlines()

    for line in lines:
        content = line.strip()
        if content == "":
            stacks.append(current_stack.copy())
            current_stack.clear()
        else:
            current_stack.insert(0, content[1])

    return stacks


def get_move_instruction(instruction: str) -> Instruction:
    instruction = search(r"move (\d+) from (\d+) to (\d+)", instruction)

    return Instruction(times=int(instruction.group(1)),
                       from_stack=int(instruction.group(2)),
                       to_stack=int(instruction.group(3)))


def get_top_items(stacks: Sequence[Sequence[str]]) -> str:
    items = ""
    for stack in stacks:
        items += stack.pop()

    return items
