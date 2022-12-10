import re

from utils.readers import reader_split_by_line


class ElfCPU:
    def __init__(self, instructions) -> None:
        self._instructions = instructions
        self._x = 1
        self._cycle = 0
        self._instruction_idx = 0
        self.sum_signal_strength = 0
        self._cycles_remaining = 0

    def execute_cycle(self):
        if self._cycles_remaining == 0:
            next_instruction = self._instructions[self._instruction_idx]
            self._instruction_idx += 1
            if re.match("addx", next_instruction):
                self._cycles_remaining = 1
                self._delta_x = int(re.search(" (-*\d+)", next_instruction).group(1))

        else:
            self._cycles_remaining -= 1
            self._x += self._delta_x

    def draw_crt(self):
        crt_pos = (self._cycle - 1) % 40
        if crt_pos == 0:
            print()
        if abs(crt_pos - self._x) < 2:
            char = "#"
        else:
            char = "."
        print(char, end="")

    def run_instructions(self):
        while self._instruction_idx < len(self._instructions):
            self._cycle += 1
            self.draw_crt()
            if self._cycle == 20 or (self._cycle - 20) % 40 == 0:
                self.sum_signal_strength += self._cycle * self._x
            self.execute_cycle()
        print()


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    cpu = ElfCPU(inp)
    cpu.run_instructions()
    return cpu.sum_signal_strength


if __name__ == "__main__":
    input_path = "y2022/inputs/day10.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print("Part 2 solution is the message printed in terminal")
