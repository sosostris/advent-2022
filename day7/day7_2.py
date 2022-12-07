import sys
from typing import Sequence
from day7_lib import DirSize, extract_command_and_args


def get_dir_sizes(outputs: Sequence[str]) -> Sequence[DirSize]:
    dir_sizes = []

    # use stack to represent current dirs
    current_dirs = []

    for output in outputs:
        output = output.strip()

        # output is command
        if output.startswith("$"):
            command, args = extract_command_and_args(output)
            if command == "cd":
                if args == "..":
                    popped_dir = current_dirs.pop()
                    dir_sizes.append(popped_dir)
                    current_dirs[-1].size += popped_dir.size
                else:
                    current_dirs.append(DirSize(name=args, size=0))
        # output is file with size
        elif not output.startswith("dir"):
            current_dirs[-1].size += int(output.split(" ")[0])

    # do not forget to handle the last directories
    while len(current_dirs) > 0:
        popped_dir = current_dirs.pop()
        dir_sizes.append(popped_dir)

        if len(current_dirs) > 0:
            current_dirs[-1].size += popped_dir.size

    return dir_sizes


def get_dir_size_to_delete(lines: Sequence[str]) -> str:
    dir_sizes = get_dir_sizes(lines)

    # root dir was the last one to added to the stack
    need_to_free_size = 30000000 - (70000000 - dir_sizes[-1].size)

    candidate = DirSize(name="inf", size=sys.maxsize)
    for dir_size in dir_sizes:
        if need_to_free_size <= dir_size.size < candidate.size:
            candidate = dir_size

    return candidate.size


def solve() -> None:
    # file = open('sample_input_7.txt', 'r')
    file = open('input_7.txt', 'r')
    lines = file.readlines()
    print(f"Size of dir to delete is: {get_dir_size_to_delete(lines)}")


solve()
