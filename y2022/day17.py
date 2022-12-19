import numpy as np

from utils.readers import reader_split_by_line


class RockGenerator:
    def __init__(self) -> None:
        self.idx = 0

    def _horizontal_bar(self):
        return [(i, 0) for i in range(4)]

    def _plus(self):
        coords = [(i, 1) for i in range(3)]
        coords.extend([(1, 0), (1, 2)])
        return coords

    def _hook(self):
        coords = [(i, 0) for i in range(3)]
        coords.extend([(2, i) for i in range(1, 3)])
        return coords

    def _vertical_bar(self):
        return [(0, i) for i in range(4)]

    def _cube(self):
        return [(0, 0), (0, 1), (1, 0), (1, 1)]

    def next_rock(self):
        if self.idx % 5 == 0:
            rock = self._horizontal_bar()
        elif self.idx % 5 == 1:
            rock = self._plus()
        elif self.idx % 5 == 2:
            rock = self._hook()
        elif self.idx % 5 == 3:
            rock = self._vertical_bar()
        else:
            rock = self._cube()

        self.idx += 1
        return rock


class JetReader:
    def __init__(self, jet_pattern) -> None:
        self.jet_pattern = jet_pattern
        self.idx = 0

    def next_move(self):
        char = self.jet_pattern[self.idx % len(self.jet_pattern)]
        self.idx += 1
        if char == "<":
            return (-1, 0)
        else:
            return (1, 0)


def make_move(move, rock, cave):
    new_rock_pos = [(x + move[0], y + move[1]) for (x, y) in rock]
    for x, y in new_rock_pos:
        if x < 0 or x > 6 or y < 0 or cave[x, y]:
            return rock

    return new_rock_pos


def update_height(rock, current_height):
    new_height = 0
    for _, y in rock:
        if y + 1 > new_height:
            new_height = y + 1

    return max(new_height, current_height)


def solution_1(input_path):
    jet_pattern = reader_split_by_line(input_path)[0]
    jet_reader = JetReader(jet_pattern)
    cave = np.zeros((7, 10000), dtype=np.bool8)
    rock_generator = RockGenerator()
    current_height = 0
    while rock_generator.idx < 2022:
        rock = rock_generator.next_rock()
        rock = [(x + 2, y + current_height + 3) for (x, y) in rock]
        falling = True
        while falling:
            # Push
            move = jet_reader.next_move()
            rock_pos_after_push = make_move(move, rock, cave)

            # Fall
            fall = (0, -1)
            rock_pos_after_fall = make_move(fall, rock_pos_after_push, cave)
            if rock_pos_after_push == rock_pos_after_fall:
                falling = False

            rock = rock_pos_after_fall

        for coord in rock:
            cave[coord] = True

        current_height = update_height(rock, current_height)

    return current_height


def solution_2(input_path):
    jet_pattern = reader_split_by_line(input_path)[0]
    jet_reader = JetReader(jet_pattern)
    cave = np.zeros((7, 1000000), dtype=np.bool8)
    rock_generator = RockGenerator()
    current_height = 0
    while rock_generator.idx < 10 ** 9:
        rock = rock_generator.next_rock()
        rock = [(x + 2, y + current_height + 3) for (x, y) in rock]
        falling = True
        while falling:
            # Push
            move = jet_reader.next_move()
            rock_pos_after_push = make_move(move, rock, cave)

            # Fall
            fall = (0, -1)
            rock_pos_after_fall = make_move(fall, rock_pos_after_push, cave)
            if rock_pos_after_push == rock_pos_after_fall:
                falling = False

            rock = rock_pos_after_fall

        for coord in rock:
            cave[coord] = True

        current_height = update_height(rock, current_height)
        if (
            rock_generator.idx % 5 == 0
            and jet_reader.idx % len(jet_reader.jet_pattern) == 0
            and 1000000000000 % rock_generator.idx == 0
        ):
            return current_height * 1000000000000 / rock_generator.idx

    return current_height


if __name__ == "__main__":
    input_path = "y2022/inputs/day17.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
