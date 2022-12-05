import re

from utils.readers import reader_split_by_line


def split_instructions(inp):
    crate_setup = []
    for idx in range(len(inp)):
        if inp[idx] == "":
            move_instructions = inp[idx + 1 :]
            break
        else:
            crate_setup.append(inp[idx])

    return crate_setup, move_instructions


def get_initial_stacks(crate_setup):
    stacks = {}
    crate_setup = crate_setup[:-1]
    crate_setup.reverse()

    for layer in crate_setup:
        for idx in range(1, len(layer), 4):
            if layer[idx] != " ":
                stack_idx = idx // 4 + 1
                if stack_idx in stacks:
                    stacks[stack_idx].append(layer[idx])
                else:
                    stacks[stack_idx] = [layer[idx]]

    return stacks


def extract_moves(move_instructions):
    moves = []

    for instr in move_instructions:
        exp = ".* (\d+).*(\d+).*(\d+)$"
        match = re.match(exp, instr)
        groups = match.groups()
        moves.append((int(groups[1]), int(groups[2]), int(groups[0])))

    return moves


def reorder_stacks(stacks, moves):
    for move in moves:
        for _ in range(move[2]):
            crate = stacks[move[0]].pop()
            stacks[move[1]].append(crate)

    return stacks


def reorder_stacks_v2(stacks, moves):
    for move in moves:
        crates = stacks[move[0]][-move[2] :]
        stacks[move[0]] = stacks[move[0]][: -move[2]]
        stacks[move[1]].extend(crates)

    return stacks


def top_crates(stacks):
    ret_str = ""
    for key in stacks:
        ret_str += stacks[key].pop()
    return ret_str


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    crate_setup, move_instructions = split_instructions(inp)
    stacks = get_initial_stacks(crate_setup)
    moves = extract_moves(move_instructions)
    ordered_stack = reorder_stacks(stacks, moves)
    return top_crates(ordered_stack)


def solution_2(input_path):
    inp = reader_split_by_line(input_path)
    crate_setup, move_instructions = split_instructions(inp)
    stacks = get_initial_stacks(crate_setup)
    moves = extract_moves(move_instructions)
    ordered_stack = reorder_stacks_v2(stacks, moves)
    return top_crates(ordered_stack)


if __name__ == "__main__":
    input_path = "y2022/inputs/day05.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
