from utils.readers import reader_split_by_line
from y2021.day18 import solution_2


from numpy import prod


def calc_pkt_value(type, values):
    if type == 0:
        val = sum(values)
    elif type == 1:
        val = prod(values)
    elif type == 2:
        val = min(values)
    elif type == 3:
        val = max(values)
    elif type == 5:
        if values[0] > values[1]:
            val = 1
        else:
            val = 0
    elif type == 6:
        if values[0] < values[1]:
            val = 1
        else:
            val = 0
    elif type == 7:
        if values[0] == values[1]:
            val = 1
        else:
            val = 0
    else:
        raise ValueError(f"Unknown pkt type: {type}")

    return val


def decode_packets(bin_str):
    pkt_version = int(bin_str[:3], 2)
    type_id = int(bin_str[3:6], 2)
    if type_id == 4:
        cumulative_versions = pkt_version
        bin_num = ""
        next_bit = 6
        while True:
            bin_num += bin_str[next_bit + 1 : next_bit + 5]
            if bin_str[next_bit] == "1":
                next_bit += 5
            else:
                remaining_str = bin_str[next_bit + 5 :]
                pkt_value = int(bin_num, 2)
                break

    else:
        lenght_type_id = bin_str[6]
        values = []
        versions_list = []
        if lenght_type_id == "0":
            lenght = int(bin_str[7:22], 2)
            sub_packets_str = bin_str[22 : 22 + lenght]
            while (
                sub_packets_str != len(sub_packets_str) * "0"
                and len(sub_packets_str) > 4
            ):
                sub_packets_str, val, ver = decode_packets(sub_packets_str)
                values.append(val)
                versions_list.append(ver)

            remaining_str = bin_str[22 + lenght :]
        else:
            n_packets = int(bin_str[7:18], 2)
            sub_packets_str = bin_str[18:]

            for _ in range(n_packets):
                sub_packets_str, val, ver = decode_packets(sub_packets_str)
                values.append(val)
                versions_list.append(ver)
            remaining_str = sub_packets_str

        cumulative_versions = pkt_version + sum(versions_list)
        pkt_value = calc_pkt_value(type_id, values)

    return remaining_str, pkt_value, cumulative_versions


def hex2bin(hex_str):
    s = ""
    for char in hex_str:
        bits = bin(int(char, 16))[2:]
        while len(bits) < 4:
            bits = "0" + bits
        s += bits

    return s


def solution_1(hex_string):
    bin_str = hex2bin(hex_string)
    _, _, summed_versions = decode_packets(bin_str)
    return summed_versions


def solution_2(hex_string):
    bin_str = hex2bin(hex_string)
    _, value, _ = decode_packets(bin_str)
    return value


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day16.txt")[0]
    result_1 = solution_1(input)
    print(f"Solution for part 1 is: {result_1}")

    result_2 = solution_2(input)
    print(f"Solution for part 2 is: {result_2}")
