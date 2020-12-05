def load_input(path):
    seat_codes = []
    with open(path) as f:
        for line in f:
            seat_codes.append(line.strip('\n'))

    return seat_codes

def calc_id(codes):
    id_list = []
    for binary_code in codes:
        row_bin = binary_code[0:7]
        column_bin = binary_code[7:]
        row_dec = bin2dec(row_bin)
        column_dec = bin2dec(column_bin)
        id_list.append(row_dec * 8 + column_dec)

    return id_list

def bin2dec(bin):
    dec = 0
    for (idx,char) in enumerate(bin[::-1]):
        if char == 'B' or char == 'R':
            dec += 2**idx
    return dec

def find_missing_id(id_list):
    for seat in range(1024):
        if seat not in id_list and seat - 1 in id_list and seat + 1 in id_list:
            return seat


data = load_input('inputs/day05.txt')
id_list = calc_id(data)
print(f"Solution to task on is {max(id_list)}.")
print(f"The missing seat is {find_missing_id(id_list)}.")

