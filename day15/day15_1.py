from typing import Sequence, Tuple
from day15_lib import Pos, get_impossible_intervals_for_row, get_sensors_and_beacons


def get_impossible_positions_in_row(impossible_intervals: Sequence[Tuple[int, int]]) -> int:
    impossible_positions = 0
    for interval in impossible_intervals:
        impossible_positions += interval[1] - interval[0] + 1

    return impossible_positions


def get_beacon_count_in_row(row: int, beacons: Sequence[Pos]) -> int:
    x_positions = set()

    for beacon in beacons:
        if beacon.y == row and (beacon.x not in x_positions):
            x_positions.add(beacon.x)

    return len(x_positions)


def solve(row: int) -> None:
    # file = open('sample_input_15.txt', 'r')
    file = open('input_15.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    sensors, beacons = get_sensors_and_beacons(lines)
    impossible_intervals = get_impossible_intervals_for_row(row, sensors)

    number_of_impossible_positions = get_impossible_positions_in_row(impossible_intervals)
    beacon_count_in_row = get_beacon_count_in_row(row, beacons)

    print(f"Number of impossible positions: {number_of_impossible_positions - beacon_count_in_row}")


solve(2000000)
