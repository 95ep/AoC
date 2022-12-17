import re

from utils.readers import reader_split_by_line


def parse_sensor_and_beacon(lines):
    positions = []
    for line in lines:
        groups = re.match(
            r".*x=(-?\d+).*y=(-?\d+).*x=(-?\d+).*y=(-?\d+)", line
        ).groups()
        positions.append(
            ((int(groups[0]), int(groups[1])), (int(groups[2]), int(groups[3])))
        )

    return positions


def calc_manhattan_dist(positions):
    distances = []
    for sensor, beacon in positions:
        delta_x = abs(sensor[0] - beacon[0])
        delta_y = abs(sensor[1] - beacon[1])
        distances.append(delta_x + delta_y)
    return distances


def no_distress_for_row(positions, distances, row):
    no_distress = set()
    for (sensor, _), dist in zip(positions, distances):
        delta_y = row - sensor[1]
        if abs(delta_y) <= dist:
            for delta_x in range(dist - abs(delta_y) + 1):
                no_distress.add((sensor[0] + delta_x, sensor[1] + delta_y))
                no_distress.add((sensor[0] - delta_x, sensor[1] + delta_y))

    return no_distress


def get_no_distress_pos(positions, distances, row):
    no_distress = set()
    for (sensor, _), dist in zip(positions, distances):
        delta_y = row - sensor[1]
        if abs(delta_y) <= dist:
            for delta_x in range(dist - abs(delta_y) + 1):
                no_distress.add((sensor[0] + delta_x, sensor[1] + delta_y))
                no_distress.add((sensor[0] - delta_x, sensor[1] + delta_y))

    return no_distress


def solution_1(input_path, row):
    inp = reader_split_by_line(input_path)
    positions = parse_sensor_and_beacon(inp)
    dists = calc_manhattan_dist(positions)
    no_distress = no_distress_for_row(positions, dists, row)
    beacon_set = set([pos[1] for pos in positions])
    return len(no_distress - beacon_set)


def solution_2(input_path):
    inp = reader_split_by_line(input_path)
    positions = parse_sensor_and_beacon(inp)
    dists = calc_manhattan_dist(positions)


if __name__ == "__main__":
    input_path = "y2022/inputs/day15.txt"
    print(f"Answer to part 1 is: {solution_1(input_path,2000000)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
