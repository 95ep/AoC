import re

def load_input(path):
    instructions = []
    with open(path) as f:
        for line in f:
            instructions.append(line)

    return instructions


def initialize(instructions):
    memory = {}
    mask_exp = re.compile(r"mask = ([X01]{36})\n")
    val_exp = re.compile(r"mem\[(\d+)\] = (\d+)\n?")
    for instr in instructions:
        match = re.match(mask_exp, instr)
        if match:
            mask = match.groups()[0]
        else:
            mem_idx, val = re.match(val_exp, instr).groups()
            memory[mem_idx] = apply_mask(val, mask)

    return sum(memory.values())

def apply_mask(val, mask):
    bin_val = format(int(val), '036b')
    for idx, mask_bit in enumerate(mask):
        if mask_bit != 'X':
            bin_val = bin_val[:idx] + mask_bit + bin_val[idx+1:]

    return int(bin_val, 2)




instructions = load_input('inputs/day14.txt')
print(initialize(instructions))