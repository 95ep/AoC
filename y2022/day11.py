import re

from utils.readers import reader_split_by_exp


class Monkey:
    def __init__(
        self, starting_items, operation, worry_divisor, test_divisor, receivers
    ) -> None:
        self.items = starting_items
        self.operation = operation
        self.worry_divisor = worry_divisor
        self.test_divisor = test_divisor
        self.receivers = receivers

        self.n_inspections = 0

    def has_item(self):
        return len(self.items) > 0

    def throw(self):
        self.n_inspections += 1
        item = self.items.pop(0)
        item = self.operation(item) // self.worry_divisor
        item = item % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
        if item % self.test_divisor == 0:
            receiver = self.receivers[0]
        else:
            receiver = self.receivers[1]

        return item, receiver

    def receive_item(self, item):
        self.items.append(item)


def instantiate_monkeys(inp, worry_divisor=3):
    monkeys = []
    for monkey_def in inp:
        starting_items = [int(match) for match in re.findall("\d+", monkey_def[1])]
        operator = eval("lambda old: " + monkey_def[2].split("new = ")[1])
        test_divisor = int(re.search("by (\d+)", monkey_def[3]).group(1))
        receivers = [
            int(re.search("monkey (\d+)", monkey_def[4 + idx]).group(1))
            for idx in range(2)
        ]
        monkeys.append(
            Monkey(starting_items, operator, worry_divisor, test_divisor, receivers)
        )
    return monkeys


def play_keep_away(monkeys, rounds):
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.has_item():
                item, receiver = monkey.throw()
                monkeys[receiver].receive_item(item)


def calc_monkey_business(monkeys):
    n_inspections = [monkey.n_inspections for monkey in monkeys]
    n_inspections.sort()
    return n_inspections[-1] * n_inspections[-2]


def solution_1(input_path):
    inp = reader_split_by_exp(input_path, "\n")
    monkeys = instantiate_monkeys(inp)
    play_keep_away(monkeys, 20)

    return calc_monkey_business(monkeys)


def solution_2(input_path):
    inp = reader_split_by_exp(input_path, "\n")
    monkeys = instantiate_monkeys(inp, worry_divisor=1)
    play_keep_away(monkeys, 10000)

    return calc_monkey_business(monkeys)


if __name__ == "__main__":
    input_path = "y2022/inputs/day11.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
