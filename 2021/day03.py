def calc_cumulative_binary(binary_list, factor):
    cumulative_binary = [0 for _ in range(len(binary_list[0]))]
    for binary in binary_list:
        for idx, bit in enumerate(binary):
            if bit == "1":
                cumulative_binary[idx] += factor
            else:
                cumulative_binary[idx] += -factor

    return cumulative_binary


def cumulative_bin_to_bin(cumulative_binary):
    bin = ""
    for bit in cumulative_binary:
        if bit > 0:
            bin = bin + "1"
        else:
            bin = bin + "0"

    return bin


def bin_to_dec(bin):
    dec = 0
    for idx in range(len(bin)):
        if bin[-(idx + 1)] == "1":
            dec += 2 ** idx
    return dec


def load_input(path):
    binary_list = []
    with open(path) as f:
        for line in f:
            binary_list.append(line.rstrip())

    return binary_list


def filter_per_bit(binary_list, idx, desired_bit):
    new_list = []
    for binary in binary_list:
        if binary[idx] == desired_bit:
            new_list.append(binary)

    return new_list


def apply_bit_criteria(binary_list, factor):
    for idx in range(len(binary_list[0])):
        common_binary = calc_cumulative_binary(binary_list, factor)
        if common_binary[idx] < 0:
            desired_bit = "0"
        elif common_binary[idx] == 0:
            if factor < 0:
                desired_bit = "0"
            else:
                desired_bit = "1"
        else:
            desired_bit = "1"
        binary_list = filter_per_bit(binary_list, idx, desired_bit)
        if len(binary_list) == 1:
            break

    return binary_list[0]


binary_list = load_input("2021/inputs/day03.txt")
gamma_cumulative_bin = calc_cumulative_binary(binary_list, 1)
epsilon_cumulative_bin = calc_cumulative_binary(binary_list, -1)

gamma_bin = cumulative_bin_to_bin(gamma_cumulative_bin)
epsilon_bin = cumulative_bin_to_bin(epsilon_cumulative_bin)

gamma = bin_to_dec(gamma_bin)
epsilon = bin_to_dec(epsilon_bin)

print(f"Gamma: {gamma}, epsilon: {epsilon}, product: {gamma*epsilon}")

# Part 2
oxygen_binary = apply_bit_criteria(binary_list, 1)
co2_binary = apply_bit_criteria(binary_list, -1)

oxygen = bin_to_dec(oxygen_binary)
co2 = bin_to_dec(co2_binary)
print(f"oxygen: {oxygen}, co2: {co2} and product: {oxygen*co2}")
