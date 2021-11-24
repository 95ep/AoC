import numpy as np

def load_input(path):
    starting_state = []
    with open(path) as f:
        for line in f:
            starting_state.append(line.strip('\n'))

    return starting_state


def init_pocket_dim(initial_state, n_cycles):
    n_x = len(initial_state) + n_cycles * 2
    n_y = len(initial_state[0]) + n_cycles * 2
    n_z = 1 + n_cycles * 2

    pocket = np.zeros((n_x, n_y, n_z), dtype=int)

    for i1, row in enumerate(initial_state):
        for i2, element in enumerate(row):
            if element == '#':
                pocket[n_cycles + i1, n_cycles + i2, n_cycles] = 1


    return pocket

def init_pocket_dim2(initial_state, n_cycles):
    n_x = len(initial_state) + n_cycles * 2
    n_y = len(initial_state[0]) + n_cycles * 2
    n_z = 1 + n_cycles * 2
    n_w = 1 + n_cycles * 2

    pocket = np.zeros((n_x, n_y, n_z, n_w), dtype=int)

    for i1, row in enumerate(initial_state):
        for i2, element in enumerate(row):
            if element == '#':
                pocket[n_cycles + i1, n_cycles + i2, n_cycles, n_cycles] = 1

    return pocket


def update_cycle(old_pocket):
    new_pocket = old_pocket.copy()
    n_x, n_y, n_z = old_pocket.shape
    for x in range(n_x):
        for y in range(n_y):
            for z in range(n_z):
                n_neighbours = count_neighbours((x,y,z), old_pocket)
                if old_pocket[x, y, z] == 1 and (n_neighbours < 2 or 3 < n_neighbours):
                    new_pocket[x,y,z] = 0
                elif old_pocket[x, y, z] == 0 and n_neighbours == 3:
                    new_pocket[x, y, z] = 1

    return new_pocket


def update_cycle2(old_pocket):
    new_pocket = old_pocket.copy()
    n_x, n_y, n_z, n_w = old_pocket.shape
    for x in range(n_x):
        for y in range(n_y):
            for z in range(n_z):
                for w in range(n_w):
                    n_neighbours = count_neighbours2((x, y, z, w), old_pocket)
                    if old_pocket[x, y, z, w] == 1 and (n_neighbours < 2 or 3 < n_neighbours):
                        new_pocket[x, y, z, w] = 0
                    elif old_pocket[x, y, z, w] == 0 and n_neighbours == 3:
                        new_pocket[x, y, z, w] = 1

    return new_pocket


def count_neighbours(coord, pocket):
    n_x, n_y, n_z = pocket.shape
    n_neighbours = 0
    for i1 in range(coord[0]-1, coord[0]+2):
        for i2 in range(coord[1]-1, coord[1]+2):
            for i3 in range(coord[2]-1, coord[2]+2):
                if -1 < i1 and i1 < n_x:
                    if -1 < i2 and i2 < n_y:
                        if -1 < i3 and i3 < n_z:
                            if (i1, i2, i3) != coord:
                                if pocket[i1,i2,i3] == 1:
                                    n_neighbours += 1

    return n_neighbours

def count_neighbours(coord, pocket):
    n_x, n_y, n_z = pocket.shape
    n_neighbours = 0
    for i1 in range(coord[0]-1, coord[0]+2):
        for i2 in range(coord[1]-1, coord[1]+2):
            for i3 in range(coord[2]-1, coord[2]+2):
                if -1 < i1 and i1 < n_x:
                    if -1 < i2 and i2 < n_y:
                        if -1 < i3 and i3 < n_z:
                            if (i1, i2, i3) != coord:
                                if pocket[i1,i2,i3] == 1:
                                    n_neighbours += 1

    return n_neighbours

def count_neighbours2(coord, pocket):
    n_x, n_y, n_z, n_w = pocket.shape
    n_neighbours = 0
    for i1 in range(coord[0]-1, coord[0]+2):
        for i2 in range(coord[1]-1, coord[1]+2):
            for i3 in range(coord[2]-1, coord[2]+2):
                for i4 in range(coord[3]-1, coord[3]+2):
                    if -1 < i1 and i1 < n_x:
                        if -1 < i2 and i2 < n_y:
                            if -1 < i3 and i3 < n_z:
                                if -1 < i4 and i4 < n_w:
                                    if (i1, i2, i3, i4) != coord:
                                        if pocket[i1, i2, i3, i4] == 1:
                                            n_neighbours += 1

    return n_neighbours

def solve_task_1(pocket_state, n_cycles):
    for _ in range(n_cycles):
        pocket_state = update_cycle(pocket_state)

    return np.sum(pocket_state)

def solve_task_2(pocket_state, n_cycles):
    for _ in range(n_cycles):
        pocket_state = update_cycle2(pocket_state)

    return np.sum(pocket_state)


initial_state = load_input('inputs/day17.txt')
init_pocket = init_pocket_dim(initial_state, 6)

print(f"#Task1: active cubes after 6 cycles are {solve_task_1(init_pocket, 6)}")

init_pocket2 = init_pocket_dim2(initial_state, 6)

print(f"#Task 2: active cubes after 6 cycles are {solve_task_2(init_pocket2, 6)}")