from dataclasses import dataclass
from re import search
from typing import Dict, List, Mapping, Set, Tuple


@dataclass
class ValvePath:
    valve: str
    minutes: int


def compact_connections(openable_valve_rates: Mapping[str, int],
                        valve_connections: Mapping[str, Set[str]]
                        ) -> Mapping[str, Mapping[str, int]]:
    all_minutes = {}
    for valve in openable_valve_rates:
        minutes = calc_single_source_shortest_paths(valve, openable_valve_rates, valve_connections)
        all_minutes[valve] = minutes

    return all_minutes


def calc_single_source_shortest_paths(source_valve: str,
                                      openable_valve_rates: Mapping[str, int],
                                      valve_connections: Mapping[str, Set[str]]
                                      ) -> Mapping[str, int]:
    minutes = {}

    queue = []
    visited = set()
    source_valve_path = ValvePath(valve=source_valve, minutes=0)
    queue.append(source_valve_path)

    while len(queue) > 0:
        current_valve_path = queue.pop(0)
        visited.add(current_valve_path.valve)
        if current_valve_path.valve != source_valve and current_valve_path.valve in openable_valve_rates:
            minutes[current_valve_path.valve] = current_valve_path.minutes

        connected_valves = valve_connections[current_valve_path.valve]
        for connected_valve in connected_valves:
            if connected_valve not in visited:
                connected_valve_path = ValvePath(valve=connected_valve, minutes=current_valve_path.minutes + 1)
                queue.append(connected_valve_path)

    return minutes


def get_valve_connections(lines: List[str]) -> Mapping[str, Set[str]]:
    valve_connections = {}

    for line in lines:
        valve_connection = search(r"Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? (.+)", line)
        connections = set(valve_connection.group(3).split(", "))
        valve_connections[valve_connection.group(1)] = connections

    return valve_connections


def assign_indices_to_openable_valves(openable_valve_rates: Mapping[str, int]) -> Mapping[str, int]:
    return {valve: index for index, valve in enumerate(openable_valve_rates.keys())}


def get_openable_valve_rates(lines: List[str]) -> Mapping[str, int]:
    openable_valve_rates = {}
    for line in lines:
        valve_rate = search(r"Valve ([A-Z]+) has flow rate=(\d+)", line)
        if valve_rate.group(2) != "0" or valve_rate.group(1) == "AA":
            openable_valve_rates[valve_rate.group(1)] = int(valve_rate.group(2))

    return openable_valve_rates


def is_valve_open(valve_index: int, current_open_valves: int) -> bool:
    return (1 << valve_index) & current_open_valves > 0


def open_valve(valve_index: int, current_open_valves: int) -> int:
    return (1 << valve_index) | current_open_valves


class Solver:
    def __init__(self, lines: List[str]):
        self.openable_valve_rates = get_openable_valve_rates(lines)
        self.openable_valve_indices = assign_indices_to_openable_valves(self.openable_valve_rates)
        self.openable_valve_connections = compact_connections(self.openable_valve_rates, get_valve_connections(lines))
        self.releases = {}

    def max_release_by_dfs(self,
                           current_valve: str,
                           remaining_time: int, open_valves: int) -> int:
        if (current_valve, remaining_time, open_valves) in self.releases:
            return self.releases[(current_valve, remaining_time, open_valves)]

        if remaining_time <= 0:
            return 0

        max_release = 0

        if not is_valve_open(self.openable_valve_indices[current_valve], open_valves) and current_valve != "AA":
            current_valve_release = (remaining_time - 1) * self.openable_valve_rates[current_valve]
            new_open_valves = open_valve(self.openable_valve_indices[current_valve], open_valves)
            max_release = current_valve_release + self.max_release_by_dfs(
                current_valve,
                remaining_time - 1,
                new_open_valves)

        for connected_valve in self.openable_valve_connections[current_valve]:
            minutes_to_connected_valve = self.openable_valve_connections[current_valve][connected_valve]
            potential_max_release = self.max_release_by_dfs(connected_valve,
                                                            remaining_time - minutes_to_connected_valve,
                                                            open_valves)
            max_release = max(max_release, potential_max_release)

        self.releases[(current_valve, remaining_time, open_valves)] = max_release

        return max_release


def solve() -> None:
    # file = open('sample_input_16.txt', 'r')
    file = open('input_16.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    solver = Solver(lines)

    # Part 1
    # max_release = solver.max_release_by_dfs("AA", 30, 0)

    # Part 2
    max_release = 0
    number_of_openable_valves = len(solver.openable_valve_rates)
    cases = (1 << number_of_openable_valves) // 2
    for my_valves in range(0, cases):
        if my_valves % 500 == 0:
            print("{0:.2%}".format(my_valves / cases))
        elephant_valves = ((1 << number_of_openable_valves) - 1) ^ my_valves
        max_release = max(max_release, solver.max_release_by_dfs("AA", 26, my_valves) +
                          solver.max_release_by_dfs("AA", 26, elephant_valves))

    print(f"Max pressure released: {max_release}")


solve()
