import re


def load_input(path):
    exp = re.compile(r"(\d+)-(\d+) (\D): (\D+)\n")
    with open(path) as f:
        data = []
        for line in f:
            groups = re.match(exp, line).groups()
            data.append((int(groups[0]), int(groups[1]), groups[2], groups[3]))

    return data


def check_passwords(password_list):
    n_valid = 0
    for low, high, char, password in password_list:
        if int(low) <= password.count(char) <= int(high):
            n_valid += 1
    return n_valid


def check_passwords_new_policy(password_list):
    n_valid = 0
    for low, high, char, password in password_list:
        low = low - 1
        high = high - 1
        if (password[low] == char and password[high] != char) or (password[low] != char and password[high] == char):
            n_valid += 1
    return n_valid


input = load_input('inputs/day02.txt')
print(f"Number of valid passwords according to 1st policy {check_passwords(input)}")
print(f"Number of valid passwords according to 2nd policy {check_passwords_new_policy(input)}")
