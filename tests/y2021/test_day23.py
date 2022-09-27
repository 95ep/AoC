from y2021.day23 import solution_1, solution_2


def test_solution_1():
    example_input = [
        "#############",
        "#...........#",
        "###B#C#B#D###",
        "#A#D#C#A#",
        "#########",
    ]
    example_result = 12521

    calculated_solution = solution_1(example_input)
    print(f"Calculated solution is: {calculated_solution}")
    print(f"Correct solution is {example_result}")
    assert calculated_solution == example_result

    print("Tests 1 successful")


def test_solution_2():
    example_input = [
        "#############",
        "#...........#",
        "###B#C#B#D###",
        "#A#D#C#A#",
        "#########",
    ]
    example_result = 44169

    calculated_solution = solution_2(example_input)
    print(f"Calculated solution is: {calculated_solution}")
    print(f"Correct solution is {example_result}")
    assert calculated_solution == example_result

    print("Tests 2 successful")


if __name__ == "__main__":
    test_solution_1()
    test_solution_2()
