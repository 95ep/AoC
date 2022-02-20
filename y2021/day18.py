import re
from utils.readers import reader_split_by_line


class SnailfishNumber:
    def __init__(self, item_1, item_2) -> None:
        self.parent = None
        self.left_child = item_1
        self.right_child = item_2

        if type(item_1) is not int:
            self.left_child.parent = self
        if type(item_2) is not int:
            self.right_child.parent = self

    def explode(self, depth):
        if depth > 4:
            left, right = self.left_child, self.right_child
            find_left_parent(self, left)
            find_right_parent(self, right)
            if self == self.parent.left_child:
                self.parent.left_child = 0
            else:
                self.parent.right_child = 0
            return right

        if type(self.left_child) is not int:
            if self.left_child.explode(depth + 1):
                return True

        if type(self.right_child) is not int:
            if self.right_child.explode(depth + 1):
                return True

        return False

    def split(self):
        if type(self.left_child) is int:
            if self.left_child > 9:
                left = self.left_child // 2
                right = left + self.left_child % 2
                self.left_child = SnailfishNumber(left, right)
                self.left_child.parent = self
                return True
        else:
            if self.left_child.split():
                return True

        if type(self.right_child) is int:
            if self.right_child > 9:
                left = self.right_child // 2
                right = left + self.right_child % 2
                self.right_child = SnailfishNumber(left, right)
                self.right_child.parent = self
                return True
        else:
            if self.right_child.split():
                return True

        return False

    def calc_magnitude(self):
        magnitude = 0
        if type(self.left_child) is int:
            magnitude += self.left_child * 3
        else:
            magnitude += self.left_child.calc_magnitude() * 3

        if type(self.right_child) is int:
            magnitude += self.right_child * 2
        else:
            magnitude += self.right_child.calc_magnitude() * 2

        return magnitude


def add_snailfish_num(number_1, number_2):
    new_number = SnailfishNumber(number_1, number_2)
    while True:
        if new_number.explode(1):
            continue
        if new_number.split():
            continue
        break

    return new_number


def find_left_leaf(node, value):
    # Find leaf for the left value after explosion
    if type(node.right_child) is int:
        node.right_child += value
    else:
        find_left_leaf(node.right_child, value)


def find_left_parent(node, value):
    # if root
    if not node.parent:
        return
    if node.parent.right_child == node:
        if type(node.parent.left_child) is int:
            node.parent.left_child += value
        else:
            find_left_leaf(node.parent.left_child, value)
    else:
        find_left_parent(node.parent, value)


def find_right_leaf(node, value):
    # Find leaf for the right value after explosion
    if type(node.left_child) is int:
        node.left_child += value
    else:
        find_right_leaf(node.left_child, value)


def find_right_parent(node, value):
    # if root
    if not node.parent:
        return
    if node.parent.left_child == node:
        if type(node.parent.right_child) is int:
            node.parent.right_child += value
        else:
            find_right_leaf(node.parent.right_child, value)
    else:
        find_right_parent(node.parent, value)


def string2num(num_str):
    if num_str[1] == "[":
        item_1, num_str = string2num(num_str[1:])
    else:
        item_1 = int(num_str[1])
        num_str = num_str[2:]

    if num_str[1] == "[":
        item_2, num_str = string2num(num_str[1:])
        num_str = num_str[1:]
    else:
        item_2 = int(num_str[1])
        num_str = num_str[3:]

    return SnailfishNumber(item_1, item_2), num_str


def solution_1(input):
    num, _ = string2num(input[0])
    for i in range(1, len(input)):
        addend, _ = string2num(input[i])
        num = add_snailfish_num(num, addend)

    return num.calc_magnitude()


def solution_2(input):
    all_magnitudes = []
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j:
                continue
            num_1, _ = string2num(input[i])
            num_2, _ = string2num(input[j])
            new_num = add_snailfish_num(num_1, num_2)
            all_magnitudes.append(new_num.calc_magnitude())

    return max(all_magnitudes)


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day18.txt")
    print(f"Answer to part 1 is: {solution_1(input)}")
    print(f"Answer to part 2 is: {solution_2(input)}")
