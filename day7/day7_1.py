from typing import Sequence
from day7_lib import DirSize, extract_command_and_args


def get_dir_size_sum_below_threshold(outputs: Sequence[str]) -> int:
    size_sum = 0

    # use stack to represent current dirs
    dirs = []

    for output in outputs:
        output = output.strip()

        # output is command
        if output.startswith("$"):
            command, args = extract_command_and_args(output)

            if command == "cd":
                if args == "..":
                    popped_dir = dirs.pop()
                    if popped_dir.size <= 100000:
                        size_sum += popped_dir.size
                    dirs[-1].size += popped_dir.size

                else:
                    dirs.append(DirSize(name=args, size=0))

        # output is file with size
        elif not output.startswith("dir"):
            dirs[-1].size += int(output.split(" ")[0])

    # do not forget to handle the last directories
    while len(dirs) > 0:
        popped_dir = dirs.pop()
        if popped_dir.size <= 100000:
            size_sum += popped_dir.size

        if len(dirs) > 0:
            dirs[-1].size += popped_dir.size

    return size_sum


def solve() -> None:
    # file = open('sample_input_7.txt', 'r')
    file = open('input_7.txt', 'r')
    lines = file.readlines()

    size_sum = get_dir_size_sum_below_threshold(lines)
    print(f"Total sum is: {size_sum}")


solve()
