from functools import lru_cache
from itertools import product
from utils.readers import reader_split_by_line


class Dice:
    def __init__(self) -> None:
        self.side_up = 0
        self.n_rolls = 0

    def roll(self):
        self.side_up += 1
        self.n_rolls += 1
        if self.side_up > 100:
            self.side_up = 1
        return self.side_up


class Player:
    def __init__(self, name, starting_pos, dice) -> None:
        self.name = name
        self.pos = starting_pos - 1
        self.score = 0
        self.dice = dice

    def move(self):
        rolls = self.dice.roll() + self.dice.roll() + self.dice.roll()
        new_pos = (self.pos + rolls) % 10
        self.score += new_pos + 1
        self.pos = new_pos


def solution_1(input):
    start = (int(input[0].split(":")[1].strip()), int(input[1].split(":")[1].strip()))
    dice = Dice()
    player_1 = Player("player 1", start[0], dice)
    player_2 = Player("player 2", start[1], dice)
    while True:
        player_1.move()
        if player_1.score > 999:
            return player_2.score * dice.n_rolls

        player_2.move()
        if player_2.score > 999:
            return player_1.score * dice.n_rolls


@lru_cache(maxsize=None)
def play_quant_game(positions, scores):
    n_wins_1 = 0
    n_wins_2 = 0
    for prod_1 in product([1, 2, 3], repeat=3):
        pos_1 = (positions[0] + sum(prod_1)) % 10
        score_1 = scores[0] + pos_1 + 1
        if score_1 > 20:
            n_wins_1 += 1
            continue

        for prod_2 in product([1, 2, 3], repeat=3):
            pos_2 = (positions[1] + sum(prod_2)) % 10
            score_2 = scores[1] + pos_2 + 1

            if score_2 > 20:
                n_wins_2 += 1
            else:
                tmp_wins_1, tmp_wins_2 = play_quant_game(
                    (pos_1, pos_2), (score_1, score_2)
                )
                n_wins_1 += tmp_wins_1
                n_wins_2 += tmp_wins_2

    return n_wins_1, n_wins_2


def solution_2(input):
    start = (
        int(input[0].split(":")[1].strip()) - 1,
        int(input[1].split(":")[1].strip()) - 1,
    )
    n_wins_1, n_wins_2 = play_quant_game(start, (0, 0))
    if n_wins_1 > n_wins_2:
        return n_wins_1
    else:
        return n_wins_2


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day21.txt")
    print(f"Answer to part 1 is: {solution_1(input)}")
    print(f"Answer to part 2 is: {solution_2(input)}")
