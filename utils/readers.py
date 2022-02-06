import re


def reader_split_by_line(path):
    inputs = []
    with open(path) as f:
        for line in f:
            inputs.append(line.rstrip())

    return inputs


def reader_split_by_exp(path, exp):
    input = []
    sub_list = []
    with open(path) as f:
        for line in f:
            if re.match(exp, line):
                if sub_list:
                    input.append(sub_list)
                sub_list = []

            else:
                sub_list.append(line.rstrip())

    input.append(sub_list)

    return input
