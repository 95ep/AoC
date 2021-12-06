import numpy as np


def load_input(path):
    with open(path) as f:
        tmp = [int(i) for i in f.readline().rstrip().split(",")]
        return np.array(tmp, dtype=int)


def simluate_growth(days, fish_list):
    fishes_per_age = [0 for _ in range(9)]
    for fish in fish_list:
        fishes_per_age[fish] += 1

    for _ in range(days):
        new_fishes_per_age = [0 for _ in range(9)]
        new_fishes_per_age[6] = fishes_per_age[0]
        new_fishes_per_age[8] = fishes_per_age[0]
        for idx in range(0, 8):
            new_fishes_per_age[idx] += fishes_per_age[idx + 1]

        fishes_per_age = new_fishes_per_age

    return sum(fishes_per_age)


fish_list = load_input("2021/inputs/day06.txt")
print(f"Numer of fishes after 80 days are: {simluate_growth(80, fish_list)}")
print(f"Numer of fishes after 256 days are: {simluate_growth(256, fish_list)}")
