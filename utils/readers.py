def reader_split_by_line(path):
    inputs = []
    with open(path) as f:
        for line in f:
            inputs.append(line.rstrip())

    return inputs
