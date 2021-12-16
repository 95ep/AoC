import numpy as np


def load_input(path):
    grid = np.zeros((10, 10), dtype=int)
    with open(path) as f:
        for i1, line in enumerate(f):
            for i2, char in enumerate(line.rstrip()):
                grid[i1, i2] = int(char)

    return grid


def model_flashes(energy_grid, n_cycles):
    n_flashes = 0
    for cycle in range(n_cycles):
        energy_grid += 1
        has_flashed = energy_grid > 9
        x_indices, y_indices = has_flashed.nonzero()
        n_flashes += len(x_indices)
        queue = [(x, y) for x, y in zip(x_indices, y_indices)]
        while len(queue) > 0:
            x, y = queue.pop()
            neighbours = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
                (x - 1, y + 1),
                (x - 1, y - 1),
                (x + 1, y + 1),
                (x + 1, y - 1),
            ]
            for i1, i2 in neighbours:
                if i1 > -1 and i1 < 10 and i2 > -1 and i2 < 10:
                    energy_grid[i1, i2] += 1

            new_flashes = np.logical_and(energy_grid > 9, ~has_flashed)
            has_flashed[new_flashes] = True
            x_indices, y_indices = new_flashes.nonzero()
            n_flashes += len(x_indices)
            queue.extend([(x, y) for x, y in zip(x_indices, y_indices)])

        energy_grid[has_flashed] = 0
        if np.count_nonzero(has_flashed) == 100:
            print(f"Syncronized flash in cycle {cycle+1}")

    return n_flashes


energy_grid = load_input("2021/inputs/day11.txt")
n_flashes = model_flashes(energy_grid, 305)
print(n_flashes)
