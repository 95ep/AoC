import re

from utils.readers import reader_split_by_line


def parse_valves_and_tunnels(lines):
    valves = {}
    tunnels = {}
    for line in lines:
        groups = re.match(
            r"Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)",
            line,
        ).groups()
        flow = int(groups[1])
        if flow > 0:
            valves[groups[0]] = flow
        tunnels[groups[0]] = [dest for dest in groups[2].split(", ")]

    return valves, tunnels


def calc_distance_between_valves(start, end, tunnels, prev_visited):
    prev_visited.add(start)
    if end in tunnels[start]:
        return 1
    else:
        possible_paths = []
        for neighbour in tunnels[start]:
            if neighbour not in prev_visited:
                dist = calc_distance_between_valves(
                    neighbour, end, tunnels, prev_visited.copy()
                )
                if dist is not None:
                    possible_paths.append(dist)

        if len(possible_paths) > 0:
            return min(possible_paths) + 1
        else:
            return None


def calc_find_all_distances(tunnels, valves):
    distances = {}
    for start in valves.keys():
        distances_sub = {}
        for end in tunnels.keys():
            if start == end:
                continue
            distances_sub[end] = calc_distance_between_valves(
                start, end, tunnels, set()
            )

        distances[start] = distances_sub

    return distances


def calc_most_pressure_released(current, valves, dists, opened, remaining_time):
    opened.add(current)
    released_potentials = []
    for valve, flow in valves.items():
        if valve not in opened and flow > 0:
            new_time_remaining = remaining_time - dists[current][valve] - 1
            if new_time_remaining > -1:
                released_potentials.append(
                    calc_most_pressure_released(
                        valve, valves, dists, opened.copy(), new_time_remaining
                    )
                )

    released = valves[current] * remaining_time
    if len(released_potentials) > 0:
        released += max(released_potentials)

    return released


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    valves, tunnels = parse_valves_and_tunnels(inp)
    valves["AA"] = 0
    distances = calc_find_all_distances(tunnels, valves)
    remaining_time = 30
    opened = set()

    return calc_most_pressure_released("AA", valves, distances, opened, remaining_time)


def solution_2(input_path):
    pass


if __name__ == "__main__":
    input_path = "y2022/inputs/day16.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
