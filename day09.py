def load_input(path):
    xmas_data = []
    with open(path) as f:
        for line in f:
            xmas_data.append(int(line))

    return xmas_data


def possible_pairs(preamble_len):
    pairs = []
    for i1 in range(preamble_len):
        for i2 in range(i1 + 1, preamble_len):
            pairs.append((i1 + 1, i2 + 1))

    return pairs


def first_invalid_entry(input, pairs, preamble):
    for idx in range(preamble, len(input)):
        is_combination = False
        for pair in pairs:
            if input[idx] == (input[idx-pair[0]] + input[idx-pair[1]]):
                is_combination = True
                break

        if not is_combination:
            return input[idx]


def find_contigous_range(data, invalid_number):
    for idx1 in range(len(data)):
        contiguous_sum = 0
        for idx2 in range(idx1, len(data)):
            contiguous_sum += data[idx2]
            if contiguous_sum == invalid_number:
                return idx1, idx2
            elif contiguous_sum > invalid_number:
                break



def find_weakness(data, invalid_number):
    lower_idx, higher_idx = find_contigous_range(data, invalid_number)
    contigous_range = data[lower_idx:higher_idx+1]
    weakness = min(contigous_range) + max(contigous_range)
    return weakness


data = load_input('inputs/day09.txt')
pairs = possible_pairs(25)

first_invalid = first_invalid_entry(data, pairs, 25)
print(first_invalid)
print(find_weakness(data, first_invalid))