import re
import numpy as np


def load_input(path):
    instructions = []
    exp  = r"(\D)(\d+)\n?"
    with open(path) as f:
        for line in f:
            instr, val = re.match(exp, line).groups()
            instructions.append((instr, int(val)))

    return instructions


def calc_pos(instructions):
    north = 0
    east = 0
    angle = 0
    for instr, val in instructions:
        if  instr == 'N':
            north += val

        elif  instr == 'S':
            north -= val

        elif  instr == 'E':
            east += val

        elif  instr == 'W':
            east -= val

        elif  instr == 'L':
            angle += val

        elif  instr == 'R':
            angle -= val

        else:
            angle = angle % 360
            if angle == 0:
                east += val

            elif angle == 90:
                north += val

            elif angle == 180:
                east -= val

            elif angle == 270:
                north -= val

            else:
                raise ValueError

    return abs(east) + abs(north)

def calc_pos2(instructions):
    north = 0
    east = 0
    wp_north = 1
    wp_east = 10
    for instr, val in instructions:
        if  instr == 'N':
            wp_north += val

        elif  instr == 'S':
            wp_north -= val

        elif  instr == 'E':
            wp_east += val

        elif  instr == 'W':
            wp_east -= val

        elif  instr == 'L' or instr == 'R':
            if instr == 'R':
                val = -val

            old_east = wp_east
            old_north = wp_north
            rad = val / 360 * 2 * np.pi

            wp_east = old_east * np.cos(rad) - old_north * np.sin(rad)
            wp_north = old_east * np.sin(rad) + old_north * np.cos(rad)

        else:
            east += val * wp_east
            north += val * wp_north

    return int(np.around( abs(east) + abs(north)))


instructions = load_input('inputs/day12.txt')
print(f"The Manhattan distance according the 1st rules are: {calc_pos(instructions)}")
print(f"The Manhattan distance according the 2nd rules are: {calc_pos2(instructions)}")