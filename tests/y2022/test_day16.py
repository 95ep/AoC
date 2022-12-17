import time
from y2022.day16 import solution_1, solution_2


def test_solution_1():
    example_input_path = "tests/y2022/inputs/day16.txt"
    example_results = 1651
    assert solution_1(example_input_path) == example_results
    print("Tests 1 successful")


def test_solution_2():
    example_input_path = "tests/y202x/inputs/dayXX.txt"
    example_result = 1707
    assert solution_2(example_input_path) == example_result
    print("Tests 2 successful")


if __name__ == "__main__":
    tic = time.time()
    test_solution_1()
    toc = time.time()
    print(f"****** Test 1 completed in {toc-tic} seconds! ********")

    tic = time.time()
    test_solution_2()
    toc = time.time()
    print(f"****** Test 2 completed in {toc-tic} seconds! ********")