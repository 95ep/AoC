import numpy as np

from utils.readers import reader_split_by_line


def construct_tree_grid(inp):
    grid = []
    for line in inp:
        grid.append([int(t) for t in line])

    return np.array(grid)


def find_visible_in_line(line):
    visible = np.zeros(line.shape, np.bool8)
    current_highest = -1
    for idx in range(line.shape[0]):
        if line[idx] > current_highest:
            visible[idx] = True
            current_highest = line[idx]

    return visible


def calc_view(line):
    view_range = 0

    current_height = line[0]
    for idx in range(1, line.shape[0]):
        if line[idx] < current_height:
            view_range += 1
        else:
            view_range += 1
            break
    return view_range


def find_visible_trees(grid):
    visible = np.zeros(grid.shape, np.bool8)
    for r_idx in range(grid.shape[0]):
        visible_row = find_visible_in_line(grid[r_idx, :])
        visible[r_idx, :] = visible[r_idx, :] | visible_row
        visible_row_reverse = find_visible_in_line(grid[r_idx, ::-1])
        visible[r_idx, ::-1] = visible[r_idx, ::-1] | visible_row_reverse
    for c_idx in range(grid.shape[1]):
        visible_col = find_visible_in_line(grid[:, c_idx])
        visible[:, c_idx] = visible[:, c_idx] | visible_col
        visible_col_reverse = find_visible_in_line(grid[::-1, c_idx])
        visible[::-1, c_idx] = visible[::-1, c_idx] | visible_col_reverse

    return visible


def calc_scenic_score(grid):
    top_score = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            view_dist_right = calc_view(grid[i, j::])
            view_dist_left = calc_view(grid[i, j::-1])
            view_dist_down = calc_view(grid[i::, j])
            view_dist_up = calc_view(grid[i::-1, j])
            view_score = (
                view_dist_right * view_dist_left * view_dist_down * view_dist_up
            )
            if view_score > top_score:
                top_score = view_score

    return top_score


def solution_1(input_path):
    raw_inp = reader_split_by_line(input_path)
    tree_grid = construct_tree_grid(raw_inp)
    visible_tree = find_visible_trees(tree_grid)
    return visible_tree.sum()


def solution_2(input_path):
    raw_inp = reader_split_by_line(input_path)
    tree_grid = construct_tree_grid(raw_inp)
    return calc_scenic_score(tree_grid)


if __name__ == "__main__":
    input_path = "y2022/inputs/day08.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
