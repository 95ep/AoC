from y2021.day21 import solution_1, solution_2


def test_solution_1():
    example_input = ["Player 1 starting position: 4", "Player 2 starting position: 8"]
    example_result = 739785
    assert solution_1(example_input) == example_result

    print("Tests 1 successful")


def test_solution_2():
    example_input = ["Player 1 starting position: 4", "Player 2 starting position: 8"]
    example_result = 444356092776315
    assert solution_2(example_input) == example_result

    print("Tests 2 successful")


if __name__ == "__main__":
    test_solution_1()
    test_solution_2()
