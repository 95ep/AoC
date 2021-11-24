def load_input(path):
    adapters_list = []
    with open(path) as f:
        for line in f:
            adapters_list.append(int(line))

    return sorted(adapters_list)

def count_diffs(adapters):
    adapters.append(adapters[-1] + 3)
    n_one_diffs = 0
    n_three_diffs = 0
    prev = 0
    for adapter in adapters:
        diff= adapter - prev
        if diff == 1:
            n_one_diffs += 1
        elif diff == 3:
            n_three_diffs += 1

        prev = adapter

    return n_one_diffs * n_three_diffs


def count_path(adapters):
    jolts = adapters.copy()
    jolts.reverse()
    jolts.append(0)

    n_adapters = len(jolts)
    n_paths = [0 for i in range(n_adapters)]
    n_paths[0] = 1

    for idx in range(n_adapters-1):
        curr = jolts[idx]
        if jolts[idx + 1] in [curr - 1, curr - 2, curr - 3]:
            n_paths[idx + 1] += n_paths[idx]
        if (idx + 2) < n_adapters and jolts[idx + 2] in [curr - 2, curr - 3]:
            n_paths[idx + 2] += n_paths[idx]
        if (idx + 3) < n_adapters and jolts[idx + 3] == curr - 3:
            n_paths[idx + 3] += n_paths[idx]

    return n_paths[-1]


adapters = load_input('inputs/day10.txt')
print(f"Task 1: The product of the 1-jolt and 3-jolt diffs are: {count_diffs(adapters)}" )
print(f"Task 2: The number of possible arrangements are: {count_path(adapters)}")