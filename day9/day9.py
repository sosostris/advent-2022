from typing import Sequence, Set
from day9_lib import Move, Pos, get_move, move_head, pull_next_knot


def move_knots(move: Move, knot_poses: Sequence[Pos], positions: Set[Pos]) -> None:
    for i in range(0, move.times):
        move_head(move.direction, knot_poses[0])
        for j in range(1, len(knot_poses)):
            pull_next_knot(knot_poses[j - 1], knot_poses[j])

        positions.add(Pos(x=knot_poses[-1].x, y=knot_poses[-1].y))


def get_covered_positions(moves: Sequence[str], number_of_knots: int) -> Set[Pos]:
    positions = set()
    positions.add(Pos(x=0, y=0))

    knot_poses = []

    for i in range(0, number_of_knots):
        original_knot_pos = Pos(x=0, y=0)
        knot_poses.append(original_knot_pos)

    for move in moves:
        move = get_move(move.strip())
        move_knots(move, knot_poses, positions)

    return positions


def solve(k: int) -> None:
    # file = open('sample_input_9.txt', 'r')
    file = open('input_9.txt', 'r')
    lines = file.readlines()

    covered_positions = get_covered_positions(lines, k)
    print(f"Number of covered positions: {len(covered_positions)}")


solve(10)
