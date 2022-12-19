from abc import ABC, abstractmethod
from typing import List, Sequence
from dataclasses import dataclass


@dataclass
class RockPos:
    x: int
    y: int


class Rock(ABC):
    def __init__(self, height: int, pos: RockPos):
        self.height = height
        self.pos = pos

    @abstractmethod
    def move_left(self, cave: Sequence[Sequence[int]]) -> None:
        pass

    @abstractmethod
    def move_right(self, cave: Sequence[Sequence[int]]) -> None:
        pass

    @abstractmethod
    def move_down(self, cave: Sequence[Sequence[int]]) -> bool:
        pass

    @abstractmethod
    def add_rock_to_cave(self, cave: List[List[int]]) -> None:
        pass


class RockOne(Rock):

    def move_left(self, cave: Sequence[Sequence[int]]):
        # check the left slot the rock is going to move into
        if self.pos.x > 0 and cave[self.pos.y][self.pos.x - 1] == 0:
            self.pos.x -= 1

    def move_right(self, cave: Sequence[Sequence[int]]):
        # check the right slot the rock is going to move into
        if self.pos.x + 3 < 6 and cave[self.pos.y][self.pos.x + 4] == 0:
            self.pos.x += 1

    def move_down(self, cave: Sequence[Sequence[int]]) -> bool:
        # check all the down slots the rock is going to move into
        if self.pos.y > 0 and cave[self.pos.y - 1][self.pos.x:self.pos.x + 4] == [0, 0, 0, 0]:
            self.pos.y -= 1
            return True
        return False

    def add_rock_to_cave(self, cave: List[List[int]]) -> None:
        cave[self.pos.y][self.pos.x:self.pos.x + 4] = [1, 1, 1, 1]


class RockTwo(Rock):

    def move_left(self, cave: Sequence[Sequence[int]]):
        if self.pos.x > 0 \
                and cave[self.pos.y][self.pos.x] == 0 \
                and cave[self.pos.y + 1][self.pos.x - 1] == 0 \
                and cave[self.pos.y + 2][self.pos.x] == 0:
            self.pos.x -= 1

    def move_right(self, cave: Sequence[Sequence[int]]):
        if self.pos.x + 2 < 6 \
                and cave[self.pos.y][self.pos.x + 2] == 0 \
                and cave[self.pos.y + 1][self.pos.x + 3] == 0 \
                and cave[self.pos.y + 2][self.pos.x + 2] == 0:
            self.pos.x += 1

    def move_down(self, cave: Sequence[Sequence[int]]) -> bool:
        if self.pos.y > 0 \
                and cave[self.pos.y - 1][self.pos.x + 1] == 0 \
                and cave[self.pos.y][self.pos.x:self.pos.x + 3] == [0, 0, 0] \
                and cave[self.pos.y + 1][self.pos.x + 1] == 0:
            self.pos.y -= 1
            return True
        return False

    def add_rock_to_cave(self, cave: List[List[int]]) -> None:
        cave[self.pos.y][self.pos.x + 1] = 1
        cave[self.pos.y + 1][self.pos.x:self.pos.x + 3] = [1, 1, 1]
        cave[self.pos.y + 2][self.pos.x + 1] = 1


class RockThree(Rock):

    def move_left(self, cave: Sequence[Sequence[int]]):
        if self.pos.x > 0 \
                and cave[self.pos.y][self.pos.x - 1] == 0 \
                and cave[self.pos.y + 1][self.pos.x + 1] == 0 \
                and cave[self.pos.y + 2][self.pos.x + 1] == 0:
            self.pos.x -= 1

    def move_right(self, cave: Sequence[Sequence[int]]):
        if self.pos.x + 2 < 6 \
                and cave[self.pos.y][self.pos.x + 3] == 0 \
                and cave[self.pos.y + 1][self.pos.x + 3] == 0 \
                and cave[self.pos.y + 2][self.pos.x + 3] == 0:
            self.pos.x += 1

    def move_down(self, cave: Sequence[Sequence[int]]) -> bool:
        if self.pos.y > 0 and cave[self.pos.y - 1][self.pos.x:self.pos.x + 3] == [0, 0, 0]:
            self.pos.y -= 1
            return True
        return False

    def add_rock_to_cave(self, cave: List[List[int]]) -> None:
        cave[self.pos.y][self.pos.x:self.pos.x + 3] = [1, 1, 1]
        cave[self.pos.y + 1][self.pos.x + 2] = 1
        cave[self.pos.y + 2][self.pos.x + 2] = 1


class RockFour(Rock):

    def move_left(self, cave: Sequence[Sequence[int]]):
        if self.pos.x > 0 \
                and cave[self.pos.y][self.pos.x - 1] == 0 \
                and cave[self.pos.y + 1][self.pos.x - 1] == 0 \
                and cave[self.pos.y + 2][self.pos.x - 1] == 0 \
                and cave[self.pos.y + 3][self.pos.x - 1] == 0:
            self.pos.x -= 1

    def move_right(self, cave: Sequence[Sequence[int]]):
        if self.pos.x < 6 \
                and cave[self.pos.y][self.pos.x + 1] == 0 \
                and cave[self.pos.y + 1][self.pos.x + 1] == 0 \
                and cave[self.pos.y + 2][self.pos.x + 1] == 0 \
                and cave[self.pos.y + 3][self.pos.x + 1] == 0:
            self.pos.x += 1

    def move_down(self, cave: Sequence[Sequence[int]]) -> bool:
        if self.pos.y > 0 and cave[self.pos.y - 1][self.pos.x] == 0:
            self.pos.y -= 1
            return True
        return False

    def add_rock_to_cave(self, cave: List[List[int]]) -> None:
        cave[self.pos.y][self.pos.x] = 1
        cave[self.pos.y + 1][self.pos.x] = 1
        cave[self.pos.y + 2][self.pos.x] = 1
        cave[self.pos.y + 3][self.pos.x] = 1


class RockFive(Rock):

    def move_left(self, cave: Sequence[Sequence[int]]):
        if self.pos.x > 0 and cave[self.pos.y][self.pos.x - 1] == 0 and cave[self.pos.y + 1][self.pos.x - 1] == 0:
            self.pos.x -= 1

    def move_right(self, cave: Sequence[Sequence[int]]):
        if self.pos.x + 1 < 6 and cave[self.pos.y][self.pos.x + 2] == 0 and cave[self.pos.y + 1][self.pos.x + 2] == 0:
            self.pos.x += 1

    def move_down(self, cave: Sequence[Sequence[int]]) -> bool:
        if self.pos.y > 0 and cave[self.pos.y - 1][self.pos.x:self.pos.x + 2] == [0, 0]:
            self.pos.y -= 1
            return True
        return False

    def add_rock_to_cave(self, cave: List[List[int]]) -> None:
        cave[self.pos.y][self.pos.x:self.pos.x + 2] = [1, 1]
        cave[self.pos.y + 1][self.pos.x:self.pos.x + 2] = [1, 1]


def init_cave() -> List[List[int]]:
    cave = []
    for i in range(0, 7):
        cave.append([0, 0, 0, 0, 0, 0, 0])

    return cave


def create_rock(rock_index: int, pos: RockPos) -> Rock:
    if rock_index == 0:
        return RockOne(1, pos)
    if rock_index == 1:
        return RockTwo(3, pos)
    if rock_index == 2:
        return RockThree(3, pos)
    if rock_index == 3:
        return RockFour(4, pos)
    return RockFive(2, pos)


def get_height_of_rock_tower(cave: List[List[int]], jet_pattern: str, rocks: int) -> int:
    jet_pattern_pos = 0
    current_top = -1

    for i in range(0, rocks):
        rock_index = i % 5
        rock_pos = RockPos(2, current_top + 4)
        rock = create_rock(rock_index, rock_pos)

        can_fall = True

        while can_fall:
            jet_pattern_pos = jet_pattern_pos % len(jet_pattern)
            jet_direction = jet_pattern[jet_pattern_pos]
            jet_pattern_pos += 1
            if jet_direction == "<":
                rock.move_left(cave)
            elif jet_direction == ">":
                rock.move_right(cave)

            if not rock.move_down(cave):
                can_fall = False

        rock.add_rock_to_cave(cave)
        current_top = max(current_top, rock.pos.y + rock.height - 1)

        while len(cave) <= current_top + 7:
            cave.append([0, 0, 0, 0, 0, 0, 0])

    # for row in reversed(cave):
    #     print(''.join(["." if c == 0 else "#" for c in row]))
    # print(f"Next jet pattern pos: {jet_pattern_pos}")
    # print(f"Current rock index: {rock_index}")

    return current_top + 1