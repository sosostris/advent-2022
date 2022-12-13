from typing import Optional, Sequence
from dataclasses import dataclass


@dataclass
class Instruction:
    command: str
    value: Optional[int]


def get_instruction(line: str) -> Instruction:
    line = line.strip()
    if line == "noop":
        return Instruction(command="noop", value=None)
    else:
        command_and_value = line.split(" ")
        return Instruction(command=command_and_value[0], value=int(command_and_value[1]))


def calc_x_at_cycle_starts(instructions: Sequence[Instruction]) -> Sequence[int]:
    x_at_cycles = [1]
    current_cycle = 1

    for instruction in instructions:
        if instruction.command == "noop":
            x_at_cycles.append(x_at_cycles[current_cycle - 1])
            current_cycle += 1
        else:
            x_at_cycles.append(x_at_cycles[current_cycle - 1])
            x_at_cycles.append(x_at_cycles[current_cycle - 1] + instruction.value)
            current_cycle += 2

    return x_at_cycles
