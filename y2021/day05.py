import re
import numpy as np


def load_input(path):
    with open(path) as f:
        vent_lines = []
        exp = re.compile(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")
        for line in f:
            m = re.search(exp, line)
            vent_lines.append([int(coord) for coord in m.groups()])

    return vent_lines


def build_grid(vent_lines):
    max_value = 0
    for line in vent_lines:
        for coord in line:
            if coord > max_value:
                max_value = coord

    return np.zeros((max_value + 1, max_value + 1), int)


def diagonal(line):
    return line[0] != line[2] and line[1] != line[3]


def add_lines(grid, vent_lines):
    for line in vent_lines:
        if not diagonal(line):
            if line[0] == line[2]:
                start_idx = min([line[1], line[3]])
                end_idx = max([line[1], line[3]]) + 1
                for i in range(start_idx, end_idx):
                    grid[i, line[0]] += 1
            else:
                start_idx = min([line[0], line[2]])
                end_idx = max([line[0], line[2]]) + 1
                for i in range(start_idx, end_idx):
                    grid[line[1], i] += 1

    return grid


def add_lines_v2(grid, vent_lines):
    for line in vent_lines:
        if not diagonal(line):
            if line[0] == line[2]:
                start_idx = min([line[1], line[3]])
                end_idx = max([line[1], line[3]]) + 1
                for i in range(start_idx, end_idx):
                    grid[i, line[0]] += 1
            else:
                start_idx = min([line[0], line[2]])
                end_idx = max([line[0], line[2]]) + 1
                for i in range(start_idx, end_idx):
                    grid[line[1], i] += 1
        else:
            k = int((line[3] - line[1]) / (line[2] - line[0]))
            m = line[1] - k * line[0]

            if line[2] > line[0]:
                for x in range(line[0], line[2] + 1):
                    grid[k * x + m, x] += 1
            else:
                for x in range(line[2], line[0] + 1):
                    grid[k * x + m, x] += 1

    return grid


vent_lines = load_input("2021/inputs/day05.txt")
grid = build_grid(vent_lines)
grid = add_lines(grid, vent_lines)
print(f"N overlaps {(grid > 1).sum()}")
grid_2 = build_grid(vent_lines)
grid_2 = add_lines_v2(grid_2, vent_lines)
print(f"N overlaps {(grid_2 > 1).sum()}")
