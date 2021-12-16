def load_input(path):
    depths = []
    with open(path) as f:
        for line in f:
            depths.append(int(line))

    return depths


def n_increasing_depth(depths, window):
    n_increases = 0
    for idx in range(window, len(depths)):
        prev_window = sum(depths[idx - window : idx])
        current_window = sum(depths[idx - window + 1 : idx + 1])
        if current_window > prev_window:
            n_increases += 1

    return n_increases


depths = load_input("2021/inputs/day01.txt")
print(f"The depth increases {n_increasing_depth(depths, 1)} times with window=1")
print(f"The depth increases {n_increasing_depth(depths, 3)} times with window=3")
