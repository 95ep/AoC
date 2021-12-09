import numpy as np


def load_input(path):
    heightmap = []
    with open(path) as f:
        for line in f:
            row = [int(i) for i in line.rstrip()]
            heightmap.append(row)

    return heightmap


def find_lowpoints(heightmap):
    n_rows = len(heightmap)
    n_columns = len(heightmap[0])
    lowpoints = []
    for i1, row in enumerate(heightmap):
        for i2, height in enumerate(row):
            neightbour_idx = [(i1 - 1, i2), (i1 + 1, i2), (i1, i2 - 1), (i1, i2 + 1)]
            is_lowpoint = True
            for idx1, idx2 in neightbour_idx:
                if idx1 > -1 and idx1 < n_rows and idx2 > -1 and idx2 < n_columns:
                    if not height < heightmap[idx1][idx2]:
                        is_lowpoint = False
                        break

            if is_lowpoint:
                lowpoints.append((i1, i2))

    return lowpoints


def calc_risk_level(lowpoints, heightmap):
    risk_level = 0
    for point in lowpoints:
        risk_level += heightmap[point[0]][point[1]] + 1

    return risk_level


def calc_basin_size(point, heightmap):
    n_rows = len(heightmap)
    n_columns = len(heightmap[0])
    queue = [point]
    processed_points = set()
    size = 0
    while len(queue) > 0:
        point = queue.pop()
        processed_points.add(point)
        i1, i2 = point
        if heightmap[i1][i2] != 9:
            size += 1
            neightbour_idx = [(i1 - 1, i2), (i1 + 1, i2), (i1, i2 - 1), (i1, i2 + 1)]
            for idx1, idx2 in neightbour_idx:
                if idx1 > -1 and idx1 < n_rows and idx2 > -1 and idx2 < n_columns:
                    if (idx1, idx2) not in processed_points and (
                        idx1,
                        idx2,
                    ) not in queue:
                        queue.insert(0, (idx1, idx2))

    return size


def calc_basin_product(lowpoints, heightmap):
    basin_size = []
    for point in lowpoints:
        basin_size.append(calc_basin_size(point, heightmap))

    basin_size.sort()
    prod = 1
    for size in basin_size[-3:]:
        prod *= size

    return prod


heightmap = load_input("2021/inputs/day09.txt")
lowpoints = find_lowpoints(heightmap)
sum_risk_level = calc_risk_level(lowpoints, heightmap)
print(f"The sum of the risk levels are: {sum_risk_level}")
basin_product = calc_basin_product(lowpoints, heightmap)
print(f"Product of three largest basin sizes is {basin_product}")
