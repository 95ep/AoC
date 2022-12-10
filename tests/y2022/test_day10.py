import time
from y2022.day10 import solution_1


def test_solution_1():
    example_input_path = "tests/y2022/inputs/day10.txt"
    example_results = 13140
    assert solution_1(example_input_path) == example_results
    print("Tests 1 successful")


if __name__ == "__main__":
    tic = time.time()
    test_solution_1()
    toc = time.time()
    print(f"****** Test 1 completed in {toc-tic} seconds! ********")
