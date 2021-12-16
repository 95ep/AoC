def load_input(path):
    with open(path) as f:
        numbers = [int(n) for n in f.readline().split(",")]
        _ = f.readline()
        boards = []
        board = []
        for line in f:
            if line == "\n":
                boards.append(board)
                board = []

            else:
                board.append([int(n) for n in line.split()])

    boards.append(board)
    return numbers, boards


def is_winner(number, board):
    for i1 in range(len(board)):
        for i2 in range(len(board[i1])):
            if board[i1][i2] == number:
                board[i1][i2] = None
                # check win 1st direction
                full_line = True
                for n in board[i1]:
                    if n is not None:
                        full_line = False
                        break
                if full_line:
                    return True

                # check win 2nd dirction
                full_line = True
                for i1_2 in range(len(board)):
                    if board[i1_2][i2] is not None:
                        full_line = False
                        break

                return full_line


def calc_score(number, board):
    board_sum = 0
    for row in board:
        for n in row:
            if n:  # Is not None
                board_sum += n
    return number * board_sum


def play_bingo(numbers, boards):
    for number in numbers:
        for board in boards:
            if is_winner(number, board):
                return calc_score(number, board)


def play_bingo_to_lose(numbers, boards):
    winner_boards = []

    for number in numbers:
        for board_idx in range(len(boards)):
            if not board_idx in winner_boards:
                board = boards[board_idx]
                if is_winner(number, board):
                    winner_boards.append(board_idx)
                    if len(winner_boards) == len(boards):
                        return calc_score(number, board)


numbers, boards = load_input("2021/inputs/day04.txt")
score = play_bingo(numbers, boards)
print(f"The winning score is {score}")
numbers, boards = load_input("2021/inputs/day04.txt")
score_lost = play_bingo_to_lose(numbers, boards)
print(f"Score of last board is {score_lost}")
