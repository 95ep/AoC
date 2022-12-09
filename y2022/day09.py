import re

from utils.readers import reader_split_by_line


def clean_input(raw_input):
    inp = []
    for line in raw_input:
        match = re.match("(\D) (\d+)", line)
        inp.append(match.groups())

    return inp


def update_head(pos, direction):
    if direction == "R":
        pos[0] += 1
    elif direction == "L":
        pos[0] -= 1
    elif direction == "U":
        pos[1] += 1
    else:
        pos[1] -= 1
    return pos


def update_tail(tail_pos, head_pos):
    x_delta = head_pos[0] - tail_pos[0]
    y_delta = head_pos[1] - tail_pos[1]
    if abs(x_delta) > 1 or abs(y_delta) > 1:
        if x_delta != 0:
            if x_delta > 0:
                tail_pos[0] += 1
            else:
                tail_pos[0] -= 1
        if y_delta != 0:
            if y_delta > 0:
                tail_pos[1] += 1
            else:
                tail_pos[1] -= 1

    return tail_pos


def solution_1(input_path):
    raw_inp = reader_split_by_line(input_path)
    inp = clean_input(raw_inp)

    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited_positions = set()
    visited_positions.add(tuple(tail_pos))
    for move in inp:
        for _ in range(int(move[1])):
            head_pos = update_head(head_pos, move[0])
            tail_pos = update_tail(tail_pos, head_pos)
            visited_positions.add(tuple(tail_pos))

    return len(visited_positions)


def solution_2(input_path):
    raw_inp = reader_split_by_line(input_path)
    inp = clean_input(raw_inp)

    positions = [[0, 0] for _ in range(10)]
    visited_positions = set()
    visited_positions.add((0, 0))
    for move in inp:
        for _ in range(int(move[1])):
            positions[0] = update_head(positions[0], move[0])
            for i in range(9):
                positions[i + 1] = update_tail(positions[i + 1], positions[i])
            visited_positions.add(tuple(positions[-1]))

    return len(visited_positions)


if __name__ == "__main__":
    input_path = "y2022/inputs/day09.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
