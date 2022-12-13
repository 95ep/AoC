import json

from utils.readers import reader_split_by_exp


def create_list_pairs(inp):
    pairs = []
    for pair_str in inp:
        pairs.append(json.loads(l) for l in pair_str)

    return pairs


def check_pair(left, right):
    if type(left) is list and type(right) is list:

        for l, r in zip(left, right):
            pair_result = check_pair(l, r)
            if pair_result is not None:
                return pair_result

        if len(left) > len(right):
            return False
        elif len(left) < len(right):
            return True
        else:
            return None

    elif type(left) is int and type(right) is int:
        if left < right:
            return True
        elif left == right:
            return None
        else:
            return False

    else:  # one of items is int other list
        if type(left) is int:
            left = [left]
        else:
            right = [right]

        return check_pair(left, right)


def find_correct_pairs(pairs):
    correct_pairs = []
    for idx, (left, right) in enumerate(pairs):
        if check_pair(left, right):
            correct_pairs.append(idx + 1)

    return correct_pairs


def bubble_sort(packets):
    has_swapped = True
    while has_swapped:
        has_swapped = False
        for idx in range(len(packets) - 1):
            if not check_pair(packets[idx], packets[idx + 1]):
                tmp = packets[idx]
                packets[idx] = packets[idx + 1]
                packets[idx + 1] = tmp
                has_swapped = True

    return packets


def solution_1(input_path):
    inp = reader_split_by_exp(input_path, "\n")
    pairs = create_list_pairs(inp)
    correct_pairs = find_correct_pairs(pairs)
    return sum(correct_pairs)


def solution_2(input_path):
    inp = reader_split_by_exp(input_path, "\n")
    packets = []
    for pair_str in inp:
        packets.append(json.loads(pair_str[0]))
        packets.append(json.loads(pair_str[1]))
    divider_packets = [[[2]], [[6]]]
    packets.extend(divider_packets)
    sorted_packets = bubble_sort(packets)
    # find divider
    divider_indices = []
    for idx, packet in enumerate(sorted_packets):
        if packet in divider_packets:
            divider_indices.append(idx + 1)

    # calc decoder_key
    return divider_indices[0] * divider_indices[1]


if __name__ == "__main__":
    input_path = "y2022/inputs/day13.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
