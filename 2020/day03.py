def load_input(path):
    with open(path) as f:
        data = [line.strip('\n') for line in f]
    return data

def trees_per_slope(delta_h, delta_v, map):
    idx_h, idx_v = 0, 0
    n_trees = 0
    dim_v = len(map[0])
    while idx_v < len(map):
        if map[idx_v][idx_h % dim_v] == '#':
            n_trees += 1
        idx_h += delta_h
        idx_v += delta_v
    return n_trees


data = load_input('inputs/day03.txt')

print(f"Part 1: {trees_per_slope(3, 1, data)}")

part_2_answer = trees_per_slope(1, 1, data) * trees_per_slope(3, 1, data) * trees_per_slope(5, 1, data) * \
                trees_per_slope(7, 1, data) * trees_per_slope(1, 2, data)
print(f"Part 2: {part_2_answer}")