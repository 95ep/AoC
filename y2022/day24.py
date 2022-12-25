import time
import numpy as np

from utils.priority_queue import PriorityQueue
from utils.readers import reader_split_by_line


def parse_blizzards(inp):
    blizzards = {}
    for i, row in enumerate(inp):
        for j, char in enumerate(row):
            if char in ["<", ">", "v", "^"]:
                blizzards[(i, j)] = [char]

    return blizzards


class BlizzardWalker:
    def __init__(self, inp, start, goal, start_step) -> None:
        self._blizzard_states = [parse_blizzards(inp)]
        self.rows = len(inp)
        self.columns = len(inp[0])
        self.shortest_path = (
            np.ones((self.rows, self.columns), dtype=np.int32) * np.iinfo(np.int32).max
        )
        # self.goal = (self.rows - 1, self.columns - 2)
        self.goal = goal
        self.positions = PriorityQueue()
        self.positions.add_with_priority((start, start_step), start_step)

    def _step_blizzards(self):
        new_state = {}
        for (x, y), directions in self._blizzard_states[-1].items():
            for direction in directions:
                x_new, y_new = x, y
                if direction == "<":
                    y_new -= 1
                elif direction == ">":
                    y_new += 1
                elif direction == "^":
                    x_new -= 1
                else:
                    x_new += 1

                x_new = ((x_new - 1) % (self.rows - 2)) + 1
                y_new = ((y_new - 1) % (self.columns - 2)) + 1
                if (x_new, y_new) in new_state:
                    new_state[(x_new, y_new)].append(direction)
                else:
                    new_state[(x_new, y_new)] = [direction]

        self._blizzard_states.append(new_state)

    def _get_blizzard_state(self, step):
        while len(self._blizzard_states) < step + 1:
            self._step_blizzards()

        return self._blizzard_states[step]

    def _check_bounds(self, pos):
        if pos == self.goal:
            return True
        if (
            0 < pos[0]
            and pos[0] < self.rows - 1
            and 0 < pos[1]
            and pos[1] < self.columns - 1
        ):
            return True

        return False

    def _consider_moves(self, pos, step, blizzard_state):
        new_positions = [
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1),
        ]
        n_steps = step + 1
        for new_pos in new_positions:
            if self._check_bounds(new_pos) and new_pos not in blizzard_state:
                try:
                    self.positions.add_with_priority((new_pos, n_steps), n_steps)
                except ValueError:
                    pass

        try:
            self.positions.add_with_priority((pos, step + 1), step + 1)
        except ValueError:
            pass

    def find_shortest_path(self):
        while self.shortest_path[self.goal] == np.iinfo(np.int32).max:
            pos, step = self.positions.pop()
            if step < self.shortest_path[pos]:
                self.shortest_path[pos] = step

            if pos in self._get_blizzard_state(step):
                # if incorrect wait
                continue
            self._consider_moves(pos, step, self._get_blizzard_state(step + 1))

        return self.shortest_path[self.goal]


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    goal = (len(inp) - 1, len(inp[0]) - 2)
    start = (0, 1)
    bw = BlizzardWalker(inp, start, goal, 0)
    return bw.find_shortest_path()


def solution_2(input_path):
    inp = reader_split_by_line(input_path)
    goal = (len(inp) - 1, len(inp[0]) - 2)
    start = (0, 1)
    steps_to_goal_1 = BlizzardWalker(inp, start, goal, 0).find_shortest_path()
    steps_back = BlizzardWalker(inp, goal, start, steps_to_goal_1).find_shortest_path()
    return BlizzardWalker(inp, start, goal, steps_back).find_shortest_path()


if __name__ == "__main__":
    input_path = "y2022/inputs/day24.txt"
    tic = time.time()
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    toc = time.time()
    print(f"****** Part 1 calculated in {toc-tic} seconds! ********")
    tic = time.time()
    print(f"Answer to part 2 is: {solution_2(input_path)}")
    toc = time.time()
    print(f"****** Part 2 calculated in {toc-tic} seconds! ********")
