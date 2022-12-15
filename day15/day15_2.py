from typing import Sequence, Tuple
from dataclasses import dataclass
from day15_lib import Pos, Sensor, get_impossible_intervals_for_row, get_sensors_and_beacons


@dataclass
class Scope:
    start: int
    end: int


def get_possible_intervals_in_row(row: int, sensors: Sequence[Sensor], start: int, end: int) -> Sequence[Tuple[int, int]]:
    impossible_intervals = get_impossible_intervals_for_row(row, sensors)

    possible_intervals = []
    if start < impossible_intervals[0][0]:
        possible_intervals.append((start, impossible_intervals[0][0] - 1))

    for i in range(1, len(impossible_intervals)):
        possible_intervals.append((impossible_intervals[i - 1][1] + 1, impossible_intervals[i][0] - 1))

    if end > impossible_intervals[-1][1]:
        possible_intervals.append((impossible_intervals[-1][1] + 1, end))

    return possible_intervals


def get_distress_beacon(scope: Scope, sensors: Sequence[Sensor]) -> Pos:
    for row in range(scope.start, scope.end + 1):
        possible_intervals = get_possible_intervals_in_row(row, sensors, scope.start, scope.end)
        if len(possible_intervals) > 0:
            return Pos(x=possible_intervals[0][0], y=row)


def solve(scope: Scope) -> None:
    # file = open('sample_input_15.txt', 'r')
    file = open('input_15.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    sensors, beacons = get_sensors_and_beacons(lines)
    distress_beacon_pos = get_distress_beacon(scope, sensors)

    print(f"Tuning frequency is: {distress_beacon_pos.x * 4000000 + distress_beacon_pos.y}")


solve(Scope(start=0, end=4000000))
