import numpy as np

from utils.readers import reader_split_by_line


def get_rock_coords(inp):
    occupied_points = set()
    for line in inp:
        str_coords = line.split(" -> ")
        for idx in range(len(str_coords) - 1):
            coords_1 = [int(c) for c in str_coords[idx].split(",")]
            coords_2 = [int(c) for c in str_coords[idx + 1].split(",")]
            if coords_1[0] == coords_2[0]:
                y_min = min(coords_1[1], coords_2[1])
                y_max = max(coords_1[1], coords_2[1])
                new_points = [(coords_1[0], c) for c in range(y_min, y_max + 1)]
            else:
                x_min = min(coords_1[0], coords_2[0])
                x_max = max(coords_1[0], coords_2[0])
                new_points = [(c, coords_1[1]) for c in range(x_min, x_max + 1)]

            for point in new_points:
                occupied_points.add(point)

    return occupied_points


def find_min_max(occupied_points):
    random_point = occupied_points.pop()
    x_min, x_max = random_point[0], random_point[0]
    y_min, y_max = random_point[1], random_point[1]
    occupied_points.add(random_point)

    for point in occupied_points:
        if point[0] > x_max:
            x_max = point[0]
        elif point[0] < x_min:
            x_min = point[0]
        if point[1] > y_max:
            y_max = point[1]
        elif point[1] < y_min:
            y_min = point[1]

    return x_min, x_max, y_min, y_max


def drop_sand(occupied_points, source, x_min, x_max, y_max, floor=None):
    position = source
    if position in occupied_points:
        return False
    while 1 == 1:
        if floor:
            if position[1] + 1 == floor:
                occupied_points.add(position)
                return True

        elif position[0] < x_min or position[0] > x_max:
            return False

        elif position[1] > y_max:
            return False

        # Move down
        if (position[0], position[1] + 1) not in occupied_points:
            position = (position[0], position[1] + 1)

        # Move down-left
        elif (position[0] - 1, position[1] + 1) not in occupied_points:
            position = (position[0] - 1, position[1] + 1)

        # Move down-right
        elif (position[0] + 1, position[1] + 1) not in occupied_points:
            position = (position[0] + 1, position[1] + 1)

        # Nowhere to move
        else:
            occupied_points.add(position)
            return True

    return True


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    occupied_points = get_rock_coords(inp)
    x_min, x_max, _, y_max = find_min_max(occupied_points)

    n_sand_units = 0
    while drop_sand(occupied_points, (500, 0), x_min, x_max, y_max):
        n_sand_units += 1

    return n_sand_units


def solution_2(input_path):
    inp = reader_split_by_line(input_path)
    occupied_points = get_rock_coords(inp)
    x_min, x_max, _, y_max = find_min_max(occupied_points)

    n_sand_units = 0
    while drop_sand(occupied_points, (500, 0), x_min, x_max, y_max, y_max + 2):
        n_sand_units += 1

    return n_sand_units


if __name__ == "__main__":
    input_path = "y2022/inputs/day14.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
