import re

from utils.readers import reader_split_by_line


def calc_trajectory(x_speed, y_speed, area):
    x_pos, y_pos = 0, 0

    y_high = 0
    while True:
        x_pos += x_speed
        y_pos += y_speed
        if x_speed > 0:
            x_speed -= 1
        y_speed -= 1

        if y_pos > y_high:
            y_high = y_pos

        if (
            x_pos >= area[0]
            and x_pos <= area[1]
            and y_pos >= area[2]
            and y_pos <= area[3]
        ):
            return y_high

        if x_speed == 0 and (x_pos < area[0] or x_pos > area[1] or y_pos < area[3]):
            return None


def get_trg_area(input_str):
    input_str = reader_split_by_line("y2021/inputs/day17.txt")[0]
    m = re.search(r"x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)", input_str)
    return [int(i) for i in m.groups()]


def solution_1():
    target_area = get_trg_area(reader_split_by_line("y2021/inputs/day17.txt")[0])

    higest_y = 0
    for initial_x in range(target_area[1]):
        for initial_y in range(0, 200):
            h = calc_trajectory(initial_x, initial_y, target_area)
            if h is not None and h > higest_y:
                higest_y = h

    return higest_y


def solution_2():
    target_area = get_trg_area(reader_split_by_line("y2021/inputs/day17.txt")[0])
    n_hits = 0
    for initial_x in range(target_area[1] + 1):
        for initial_y in range(target_area[2], 200):
            h = calc_trajectory(initial_x, initial_y, target_area)
            if h is not None:
                n_hits += 1

    return n_hits


print(solution_1())
print(solution_2())
