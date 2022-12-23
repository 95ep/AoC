from utils.readers import reader_split_by_line

import numpy as np
import re


class StrangelyShapedBoard:
    def __init__(self, board_layout) -> None:
        self.rows = len(board_layout)
        self.columns = max([len(row) for row in board_layout])
        self.board = np.zeros((self.rows, self.columns), dtype=np.int16)

        for i, row in enumerate(board_layout):
            for j, char in enumerate(row):
                if char == ".":
                    self.board[i, j] = 1
                elif char == "#":
                    self.board[i, j] = 2

        self.pos = (0, np.where(self.board[0] == 1)[0][0])
        self.facing = 0

    def update_facing(self, turn_direction):
        if turn_direction == "L":
            facing_increment = -1
        else:
            facing_increment = +1

        self.facing = (self.facing + facing_increment) % 4

    def _check_step(self):
        x, y = self.pos
        if self.facing == 0:
            y = (y + 1) % self.columns
            if self.board[x, y] == 0:
                y = np.where(self.board[x, :] != 0)[0][0]
        elif self.facing == 1:
            x = (x + 1) % self.rows
            if self.board[x, y] == 0:
                x = np.where(self.board[:, y] != 0)[0][0]

        elif self.facing == 2:
            y = (y - 1) % self.columns
            if self.board[x, y] == 0:
                y = np.where(self.board[x, :] != 0)[0][-1]

        else:
            x = (x - 1) % self.rows
            if self.board[x, y] == 0:
                x = np.where(self.board[:, y] != 0)[0][-1]

        if self.board[x, y] == 1:
            return (x, y)
        else:
            # Hit an obstacle
            return None

    def make_move(self, dist):
        for _ in range(int(dist)):
            new_pos = self._check_step()
            if new_pos:
                self.pos = new_pos
            else:
                break


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    board_inp = inp[:-2]
    move_inp = inp[-1]
    board = StrangelyShapedBoard(board_inp)
    move_turn_pairs = re.findall("(\d+)(\D)", move_inp)
    final_move = re.match(".*(\d+)$", move_inp).group(1)
    for dist, turn in move_turn_pairs:
        board.make_move(dist)
        board.update_facing(turn)

    board.make_move(final_move)

    return (board.pos[0] + 1) * 1000 + (board.pos[1] + 1) * 4 + board.facing


def solution_2(input_path):
    pass


if __name__ == "__main__":
    input_path = "y2022/inputs/day22.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
