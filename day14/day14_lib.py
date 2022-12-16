from typing import Mapping, Sequence, Set
from collections import defaultdict


def build_wall(lines: Sequence[str]) -> Mapping[int, Set[int]]:
    wall: Mapping[int, Set] = defaultdict(set)
    for line in lines:
        rock_poses = line.split(" -> ")
        for start, end in zip(rock_poses[:-1], rock_poses[1:]):
            start_x, start_y = [int(c) for c in start.split(",")]
            end_x, end_y = [int(c) for c in end.split(",")]

            if start_x == end_x:
                start_y, end_y = min(start_y, end_y), max(start_y, end_y)
                wall[start_x] |= set(range(start_y, end_y + 1))
            else:  # start_y == end_y
                start_x, end_x = min(start_x, end_x), max(start_x, end_x)
                for x in range(start_x, end_x + 1):
                    wall[x].add(start_y)

    return wall
