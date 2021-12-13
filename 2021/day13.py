import matplotlib.pyplot as plt
import re


def load_input(path):
    dots = set()
    folds = []
    with open(path) as f:
        for line in f:
            if line == "\n":
                break
            x, y = line.rstrip().split(",")
            dots.add((int(x), int(y)))

        pattern = re.compile(r"fold along ([xy])=(\d+)")
        for line in f:
            m = re.search(pattern, line)
            fold_axis, fold_line = m.groups()
            folds.append((fold_axis, int(fold_line)))

    return dots, folds


def fold_paper(dots, fold_axis, fold_line):
    if fold_axis == "x":
        axis_idx = 0
    else:
        axis_idx = 1

    new_dots = set()
    for dot in dots:
        if dot[axis_idx] > fold_line:
            tmp_dot = [*dot]
            tmp_dot[axis_idx] = 2 * fold_line - dot[axis_idx]
            new_dot = tuple(tmp_dot)
        else:
            new_dot = dot

        new_dots.add(new_dot)

    return new_dots


def find_code(dots, folds):
    for fold in folds:
        dots = fold_paper(dots, fold[0], fold[1])

    # Plot the resulting dots
    plt.gca().invert_yaxis()
    plt.gca().set_aspect("equal")
    plt.scatter(*zip(*dots))
    plt.show()


dots, folds = load_input("2021/inputs/day13.txt")
dots_after_one_fold = fold_paper(dots, folds[0][0], folds[0][1])
print(f"After one fold {len(dots_after_one_fold)} dots remain")
find_code(dots, folds)
