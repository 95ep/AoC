from y2021.day25 import solution_1, solution_2


def test_solution_1():
    example_input = [
        "v...>>.vv>",
        ".vv>>.vv..",
        ">>.>v>...v",
        ">>v>>.>.v.",
        "v>v.vv.v..",
        ">.>>..v...",
        ".vv..>.>v.",
        "v.v..>>v.v",
        "....v..v.>",
    ]
    example_result = 58

    assert solution_1(example_input) == example_result

    print("Tests 1 successful")


def test_solution_2():
    example_input = []
    example_result = 444356092776315
    assert solution_2(example_input) == example_result

    print("Tests 2 successful")


if __name__ == "__main__":
    test_solution_1()
    test_solution_2()
