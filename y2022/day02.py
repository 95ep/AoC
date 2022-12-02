from utils.readers import reader_split_by_line


def determine_outcome(move_1, move_2):
    if move_1 == move_2:
        return 3
    elif (move_1 + 1) % 3 == move_2:
        return 6
    else:
        return 0


def calc_score_for_round(opponent_move, our_move):
    score = our_move + 1
    score += determine_outcome(opponent_move, our_move)
    return score


def determine_move(opponent_move, outcome):
    if outcome == 0:
        our_move = (opponent_move - 1) % 3
    elif outcome == 1:
        our_move = opponent_move
    else:
        our_move = (opponent_move + 1) % 3

    return our_move


def calc_score_for_round_v2(opponent_move, outcome):
    our_move = determine_move(opponent_move, outcome)
    return calc_score_for_round(opponent_move, our_move)


def convert_to_num(instruction):
    val1 = ord(instruction[0]) - ord("A")
    val2 = ord(instruction[2]) - ord("X")
    return val1, val2


def solution_1(input_path):
    input = reader_split_by_line(input_path)
    tot_score = 0
    for instruction in input:
        opponent_move, outcome = convert_to_num(instruction)
        tot_score += calc_score_for_round(opponent_move, outcome)

    return tot_score


def solution_2(input_path):
    input = reader_split_by_line(input_path)
    tot_score = 0
    for instruction in input:
        opponent_move, outcome = convert_to_num(instruction)
        tot_score += calc_score_for_round_v2(opponent_move, outcome)

    return tot_score


if __name__ == "__main__":
    input_path = "y2022/inputs/day02.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
