from typing import Sequence, Tuple
from dataclasses import dataclass
from re import search


@dataclass
class Pos:
    x: int
    y: int


@dataclass
class Sensor:
    pos: Pos
    beacon_pos: Pos


def get_sensors_and_beacons(lines: Sequence[str]) -> Tuple[Sequence[Sensor], Sequence[Pos]]:
    sensors = []
    beacons = []

    for line in lines:
        positions = search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        sensor_pos = Pos(x=int(positions.group(1)), y=int(positions.group(2)))
        beacon_pos = Pos(x=int(positions.group(3)), y=int(positions.group(4)))
        sensor = Sensor(pos=sensor_pos, beacon_pos=beacon_pos)
        sensors.append(sensor)
        beacons.append(beacon_pos)

    return sensors, beacons


def get_impossible_intervals_for_row(row: int, sensors: Sequence[Sensor]) -> Sequence[Tuple[int, int]]:
    impossible_intervals = []
    for sensor in sensors:
        distance_between_sensor_and_beacon = abs(sensor.pos.x - sensor.beacon_pos.x) + abs(sensor.pos.y - sensor.beacon_pos.y)
        if distance_between_sensor_and_beacon - abs(sensor.pos.y - row) >= 0:
            max_distance_x = abs(distance_between_sensor_and_beacon - abs(sensor.pos.y - row))
            impossible_intervals.append((sensor.pos.x - max_distance_x, sensor.pos.x + max_distance_x))

    merged_impossible_intervals = []
    impossible_intervals.sort(key=lambda current_interval: current_interval[0])
    merged_impossible_intervals.append(impossible_intervals[0])

    for i in range(1, len(impossible_intervals)):
        if impossible_intervals[i][0] <= merged_impossible_intervals[-1][1]:
            merged_impossible_intervals[-1] = (merged_impossible_intervals[-1][0], max(merged_impossible_intervals[-1][1], impossible_intervals[i][1]))
        elif impossible_intervals[i][0] == merged_impossible_intervals[-1][1] + 1:
            merged_impossible_intervals[-1] = (merged_impossible_intervals[-1][0], impossible_intervals[i][1])
        else:
            merged_impossible_intervals.append(impossible_intervals[i])

    return merged_impossible_intervals
