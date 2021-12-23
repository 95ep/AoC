import re
import numpy as np
from utils.readers import reader_split_by_line


def parse_input(input, cube_side):
    steps = []
    offset_to_zero = cube_side // 2
    for line in input:
        m = re.match(
            r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)",
            line,
        )
        g = m.groups()
        ranges = [
            [int(g[1]), int(g[2])],
            [int(g[3]), int(g[4])],
            [int(g[5]), int(g[6])],
        ]

        for range in ranges:
            range[0] += offset_to_zero
            range[1] += offset_to_zero
            if range[0] > range[1]:
                raise ValueError
            if range[0] < 0:
                range[0] = 0
            if range[1] >= cube_side:
                range[1] = cube_side - 1
        if g[0] == "on":
            steps.append([True, *ranges])
        else:
            steps.append([False, *ranges])

    return steps


def update_cube(cube, step):
    cube[
        step[1][0] : step[1][1] + 1,
        step[2][0] : step[2][1] + 1,
        step[3][0] : step[3][1] + 1,
    ] = step[0]


def solution_1(input):
    cube_side = 101
    steps = parse_input(input, cube_side)
    cube = np.zeros((101, 101, 101), dtype=bool)
    for step in steps:
        update_cube(cube, step)
    return cube.sum()


def solution_2(input):
    pass


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day22.txt")
    print(f"Answer to part 1 is: {solution_1(input)}")
    print(f"Answer to part 2 is: {solution_2(input)}")
