from queue import Queue

def load_input(path):
    with open(path) as f:
        f.readline()
        deck1 = Queue()
        deck2 = Queue()
        for line in f:
            if line == '\n':
                break
            deck1.put(int(line))

        f.readline()
        for line in f:
            deck2.put(int(line))

    return deck1, deck2



def play_game(deck1, deck2):
    while deck1.qsize() > 0 and deck2.qsize() > 0:
        card1 = deck1.get()
        card2 = deck2.get()
        if card1 > card2:
            deck1.put(card1)
            deck1.put(card2)
        else:
            deck2.put(card2)
            deck2.put(card1)

    if deck1.qsize() > 0:
        return deck1
    else:
        return deck2


def play_recursive_game(deck1, deck2):
    round = 1
    prev_hands_1 = []
    prev_hands_2 = []

    while deck1.qsize() > 0 and deck2.qsize() > 0:
        # print("\n \n")
        # print(f"Playing round {round}")
        round += 1
        # print(f"Player 1 deck: {deck1.queue}")
        # print(f"Player 2 deck: {deck2.queue}")
        card1 = deck1.get()
        card2 = deck2.get()
        # print(f"Player 1 plays: {card1}")
        # print(f"Player 2 plays: {card2}")
        winner = 0
        for hand in prev_hands_1:
            if hand == deck1.queue:
                # win player 1
                print("Hand identical for player 1, player 1 wins")
                winner = 1
                break


        for hand in prev_hands_2:
            if hand == deck2.queue:
                # win player 1
                # print("Hand identical for player 2, player 1 wins")
                winner = 1
                break

        if winner == 0:
            prev_hands_1.append(deck1.queue.copy())
            prev_hands_2.append(deck2.queue.copy())
        else:
            deck1.put(card1)
            deck1.put(card2)
            continue


        if deck1.qsize() >= card1 and deck2.qsize() >= card2:
            # print("Playing sub-game to determine winner!")
            deck1_copy = Queue()
            deck2_copy = Queue()
            deck1_copy.queue = deck1.queue.copy()
            deck2_copy.queue = deck2.queue.copy()
            _, _, winner = play_recursive_game(deck1_copy, deck2_copy)
        elif card1 > card2:
            # print("Player 1 wins!")
            winner = 1

        else:
            # print("Player 2 wins!")
            winner = 2

        if winner == 1:
            deck1.put(card1)
            deck1.put(card2)
        else:
            deck2.put(card2)
            deck2.put(card1)

    if deck1.qsize() > 0:
        return deck1, deck2, 1
    else:
        return deck1, deck2, 2


def calc_score(deck):
    n_cards = deck.qsize()
    score = 0
    for i in range(n_cards):
        score += deck.get() * (n_cards - i)

    return score



print("===========================")
deck1, deck2 = load_input('inputs/day22.txt')
winner = play_game(deck1, deck2)
score = calc_score(winner)
print(f"Score of game is: {score}")

deck1, deck2 = load_input('inputs/day22.txt')
deck1, deck2, winner = play_recursive_game(deck1, deck2)
if winner == 1:
    score_rec = calc_score(deck1)
else:
    score_rec = calc_score(deck2)

print(f"Score 2 {score_rec}")

