def load_input(path):
    instruction_list = []
    with open(path) as f:
        for line in f:
            instr, val = line.strip('\n').split(' ')
            instruction_list.append((instr, int(val)))

    return instruction_list

def run_instructions(instructions):
    accumulator = 0
    instruction_idx = 0
    processed_instructions = []
    while instruction_idx not in processed_instructions and instruction_idx < len(instructions):
        processed_instructions.append(instruction_idx)
        instr, val = instructions[instruction_idx]
        if instr == 'acc':
            accumulator += val
            instruction_idx += 1
        elif instr == 'jmp':
            instruction_idx += val
        else:
            instruction_idx += 1

    return accumulator, instruction_idx == len(instructions)


def find_correct_instructions(corrupt_instructions):
    for idx in range(len(corrupt_instructions)):
        instr, val = instructions[idx]
        fixed_instructions = corrupt_instructions.copy()
        if instr == 'jmp':
            fixed_instructions[idx] = ('nop', val)
        elif instr == 'nop':
            fixed_instructions[idx] = ('jmp', val)
        else:
            continue

        final_accumulator, finished_successfully = run_instructions(fixed_instructions)
        if finished_successfully:
            return final_accumulator

    return None


instructions = load_input('inputs/day08.txt')
# Task 1
final_accumulator, finished_successfully = run_instructions(instructions)
print(f"Task 1: Final accumulator: {final_accumulator}, finished successfully: {finished_successfully}")
print(f"Task 2: Final accumulator: {find_correct_instructions(instructions)}")
