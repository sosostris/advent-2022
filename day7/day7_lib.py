from typing import Optional, Tuple
from dataclasses import dataclass


@dataclass
class DirSize:
    name: str
    size: int


def extract_command_and_args(output: str) -> Tuple[str, Optional[str]]:
    command_and_args = output[2:].split(" ")
    command = command_and_args[0]
    if command == "ls":
        args = None
    else:
        args = command_and_args[1]

    return command, args
