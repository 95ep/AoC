import re
from utils.readers import reader_split_by_line


def parse_input(input):
    steps = []
    for line in input:
        m = re.match(
            r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)",
            line,
        )
        g = m.groups()
        step = (
            g[0],
            (int(g[1]), int(g[2])),
            (int(g[3]), int(g[4])),
            (int(g[5]), int(g[6])),
        )
        steps.append(step)

    return steps


def get_subintervals(intervals):
    check_points = []
    for idx, interval in enumerate(intervals):
        # (coord, is_starting_point, id)
        check_points.extend(
            [
                (interval[0], True, idx),
                (interval[1] + 1, False, idx),  # Adjust for each coord being a cube
            ]
        )
    sorted_check_points = sorted(check_points, key=lambda x: x[0])

    overlapping_ids = set()
    start = None
    sub_intervals = []
    for check_point in sorted_check_points:
        if start is not None:
            if check_point[0] != start and overlapping_ids:  # Omitt empty intervals
                # if 0 in overlapping_ids:  # Omitt intervals that are part of new block
                sub_intervals.append(  # adjust back
                    ((start, check_point[0] - 1), frozenset(overlapping_ids))
                )
            if check_point[1]:  # If starting point
                overlapping_ids.add(check_point[2])
            else:  # If stopping point
                overlapping_ids.remove(check_point[2])
            start = check_point[0]

        else:  # if 1st checkpoint
            start = check_point[0]
            overlapping_ids.add(check_point[2])

    return sub_intervals


def is_on(idx_set, steps, init):
    if init:
        if 0 in idx_set and len(idx_set) > 1:
            last_instruction = max(idx_set)
            if steps[last_instruction][0] == "on":
                return True
        return False
    else:
        if len(idx_set) > 0:
            last_instruction = max(idx_set)
            if steps[last_instruction][0] == "on":
                return True
        return False


def boot_process(steps, init):
    steps = tuple(steps)
    input_boxes = [(step[1], step[2], step[3]) for step in steps]

    sub_intervals_x = get_subintervals([box[0] for box in input_boxes])
    sub_intervals_y = get_subintervals([box[1] for box in input_boxes])
    sub_intervals_z = get_subintervals([box[2] for box in input_boxes])

    # Construct all boxes
    volume = 0
    for x_interval in sub_intervals_x:
        for y_interval in sub_intervals_y:
            x_y_intersection = x_interval[1] & y_interval[1]
            # Check that at least on id overlaps
            if x_y_intersection:
                for z_interval in sub_intervals_z:
                    # Create a sub box only if at least one id overlaps
                    x_y_z_intersection = x_y_intersection & z_interval[1]

                    if is_on(x_y_z_intersection, steps, init):
                        volume += (
                            (x_interval[0][1] - x_interval[0][0] + 1)
                            * (y_interval[0][1] - y_interval[0][0] + 1)
                            * (z_interval[0][1] - z_interval[0][0] + 1)
                        )
    return volume


def solution_1(input):
    steps = parse_input(input)
    # Add init region
    steps.insert(0, ("on", (-50, 50), (-50, 50), (-50, 50)))
    return boot_process(steps, True)


def solution_2(input):
    steps = parse_input(input)
    return boot_process(steps, False)


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day22.txt")
    print(f"Solution to part 1: {solution_1(input)}")
    print(f"Solution to part 2: {solution_2(input)}")
