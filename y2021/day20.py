import numpy as np

from utils.readers import reader_split_by_exp


def create_img_mat(img_list):
    img_mat = np.zeros((len(img_list), len(img_list[0])), dtype=bool)
    for i1 in range(len(img_list)):
        for i2 in range(len(img_list[0])):
            if img_list[i1][i2] == "#":
                img_mat[i1][i2] = True

    return img_mat


def apply_enhancement(img, algo, inf_val):
    # extend edges, adding two egdes is only necessart first time
    extended_img = np.zeros((img.shape[0] + 4, img.shape[1] + 4), dtype=bool)
    extended_img[:2, :] = inf_val
    extended_img[-2:, :] = inf_val
    extended_img[:, :2] = inf_val
    extended_img[:, -2:] = inf_val
    extended_img[2:-2, 2:-2] = img
    new_img = extended_img.copy()
    # calc output
    for i1 in range(1, new_img.shape[0] - 1):
        for i2 in range(1, new_img.shape[1] - 1):
            window = extended_img[i1 - 1 : i1 + 2, i2 - 1 : i2 + 2]
            bin_str = ""
            for element in window.flatten():
                if element:
                    bin_str += "1"
                else:
                    bin_str += "0"
            algo_idx = int(bin_str, 2)
            if algo[algo_idx] == "#":
                new_img[i1, i2] = True
            else:
                new_img[i1, i2] = False

    # cal new inf_val
    if inf_val:
        new_inf_idx = 511
    else:
        new_inf_idx = 0

    if algo[new_inf_idx] == "#":
        new_inf_val = True
    else:
        new_inf_val = False

    # fix edges
    new_img[0, :] = new_inf_val
    new_img[-1, :] = new_inf_val
    new_img[:, 0] = new_inf_val
    new_img[:, -1] = new_inf_val

    return new_img, new_inf_val


def solution_1(algo, img_list):
    img_mat = create_img_mat(img_list)
    inf_val = False
    for _ in range(2):
        img_mat, inf_val = apply_enhancement(img_mat, algo, inf_val)
    return np.count_nonzero(img_mat)


def solution_2(algo, img_list):
    img_mat = create_img_mat(img_list)
    inf_val = False
    for _ in range(50):
        img_mat, inf_val = apply_enhancement(img_mat, algo, inf_val)
    return np.count_nonzero(img_mat)


if __name__ == "__main__":
    input = reader_split_by_exp("y2021/inputs/day20.txt", r"\n")
    print(f"Answer to part 1 is: {solution_1(input[0][0], input[1])}")
    print(f"Answer to part 2 is: {solution_2(input[0][0], input[1])}")
