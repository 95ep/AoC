import copy

def load_input(path):
    layout = []
    with open(path) as f:
        for line in f:
            row = []
            for char in line.strip('\n'):
                row.append(char)
            layout.append(row)

    return layout


def update_seats(grid):
    updated = True
    while updated:
        new_grid = copy.deepcopy(grid)
        updated = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_pos = grid[row][col]
                if current_pos == 'L' or current_pos == '#':
                    n_neighbours = count_neighbours(grid, row, col)
                    if n_neighbours == 0 and current_pos == 'L':
                        new_grid[row][col] = '#'
                        updated = True
                    elif n_neighbours > 3 and current_pos == '#':
                        new_grid[row][col] = 'L'
                        updated = True
        grid = new_grid

    return grid


def count_neighbours(grid, row, col):
    n_neighbours = 0
    n_rows = len(grid)
    n_cols = len(grid[0])
    if row + 1 < n_rows and grid[row+1][col] == '#':
        n_neighbours += 1
    if row + 1 < n_rows and col+1 < n_cols and grid[row+1][col+1] == '#':
        n_neighbours += 1
    if row + 1 < n_rows and col-1 > -1 and grid[row+1][col-1] == '#':
        n_neighbours += 1
    if col-1 > -1 and grid[row][col-1] == '#':
        n_neighbours += 1
    if row - 1 > -1 and col-1 > -1 and grid[row-1][col-1] == '#':
        n_neighbours += 1
    if row - 1 > -1 and grid[row-1][col] == '#':
        n_neighbours += 1
    if row - 1 > -1 and col+1 < n_cols and grid[row-1][col+1] == '#':
        n_neighbours += 1
    if col+1 < n_cols and grid[row][col+1] == '#':
        n_neighbours += 1

    return n_neighbours

def count_occupied_sets(grid):
    n_occupied = 0
    for row in grid:
        for char in row:
            if char == '#':
                n_occupied += 1
    return n_occupied


def check_neighbour_in_direction(start_x, start_y, delta_x, delta_y, grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    idx_x = start_x + delta_x
    idx_y = start_y + delta_y
    while -1 < idx_x and -1 < idx_y and idx_x < n_rows and idx_y < n_cols:
        current_pos = grid[idx_x][idx_y]
        if current_pos == '#':
            return True
        elif current_pos == 'L':
            return False
        else:
            idx_x += delta_x
            idx_y += delta_y

    return False


def count_neighbours2(grid, row, col):
    n_neighbours = 0

    if check_neighbour_in_direction(row, col, 1, 1, grid):
        n_neighbours += 1
    if check_neighbour_in_direction(row, col, 0, 1, grid):
        n_neighbours += 1
    if check_neighbour_in_direction(row, col, -1, 1, grid):
        n_neighbours += 1
    if check_neighbour_in_direction(row, col, -1, 0, grid):
        n_neighbours += 1
    if check_neighbour_in_direction(row, col, -1, -1, grid):
        n_neighbours += 1
    if check_neighbour_in_direction(row, col, 0, -1, grid):
        n_neighbours += 1
    if check_neighbour_in_direction(row, col, 1, -1, grid):
        n_neighbours += 1
    if check_neighbour_in_direction(row, col, 1, 0, grid):
        n_neighbours += 1

    return n_neighbours


def update_seats2(grid):
    updated = True
    while updated:
        new_grid = copy.deepcopy(grid)
        updated = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_pos = grid[row][col]
                if current_pos == 'L' or current_pos == '#':
                    n_neighbours = count_neighbours2(grid, row, col)
                    if n_neighbours == 0 and current_pos == 'L':
                        new_grid[row][col] = '#'
                        updated = True
                    elif n_neighbours > 4 and current_pos == '#':
                        new_grid[row][col] = 'L'
                        updated = True
        grid = new_grid

    return grid


layout = load_input('inputs/day11.txt')
grid = update_seats(layout)
print(f"Task 1: {count_occupied_sets(grid)}")
grid2 = update_seats2(layout)
print(f"Task 2: {count_occupied_sets(grid2)}")