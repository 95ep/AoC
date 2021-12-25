import numpy as np

from utils.readers import reader_split_by_line


def make_move(pos, heard, map):
    if heard == ">":
        new_pos = (pos[0], (pos[1] + 1) % map.shape[1])
    else:
        new_pos = ((pos[0] + 1) % map.shape[0], pos[1])

    if map[new_pos] == ".":
        return new_pos
    else:
        return pos


def update_heard(heard, map):
    members = np.transpose(np.where(map == heard))
    new_positions = []
    for member in members:
        new_positions.append(make_move(member, heard, map))

    new_map = map.copy()
    new_map[members.transpose()[0], members.transpose()[1]] = "."

    new_positions = np.array(new_positions, dtype=int)
    new_map[new_positions.transpose()[0], new_positions.transpose()[1]] = heard
    return new_map


def solution_1(input):
    map = np.array([[c for c in line] for line in input])
    updated = True
    step_idx = 0
    while updated:
        step_idx += 1
        new_map = update_heard(">", map)
        new_map = update_heard("v", new_map)
        updated = not (new_map == map).all()
        map = new_map

    return step_idx


def solution_2(input):
    pass


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day25.txt")
    print(f"Answer to part 1 is: {solution_1(input)}")
    print(f"Answer to part 2 is: {solution_2(input)}")
