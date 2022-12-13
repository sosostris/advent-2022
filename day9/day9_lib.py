from dataclasses import dataclass


@dataclass
class Move:
    direction: str
    times: int


@dataclass
class Pos:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def get_move(input_move: str) -> Move:
    move_detail = input_move.split(" ")
    return Move(direction=move_detail[0], times=int(move_detail[1]))


def pull_next_knot(previous_knot_pos: Pos, next_knot_pos: Pos) -> None:
    if abs(previous_knot_pos.x - next_knot_pos.x) > 1:
        if previous_knot_pos.x < next_knot_pos.x:
            next_knot_pos.x -= 1
        else:
            next_knot_pos.x += 1

        if previous_knot_pos.y > next_knot_pos.y:
            next_knot_pos.y += 1
        elif previous_knot_pos.y < next_knot_pos.y:
            next_knot_pos.y -= 1

    if abs(previous_knot_pos.y - next_knot_pos.y) > 1:
        if previous_knot_pos.y < next_knot_pos.y:
            next_knot_pos.y -= 1
        else:
            next_knot_pos.y += 1

        if previous_knot_pos.x > next_knot_pos.x:
            next_knot_pos.x += 1
        elif previous_knot_pos.x < next_knot_pos.x:
            next_knot_pos.x -= 1


def move_head(direction: str, current_head_pos: Pos) -> None:
    if direction == "U":
        current_head_pos.y -= 1
    elif direction == "D":
        current_head_pos.y += 1
    elif direction == "L":
        current_head_pos.x -= 1
    else:
        current_head_pos.x += 1
