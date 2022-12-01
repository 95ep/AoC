import time
from y2022.day01 import solution_1, solution_2


def test_solution_1():
    example_input = [
        [
            "1000",
            "2000",
            "3000",
        ],
        [
            "4000",
        ],
        [
            "5000",
            "6000",
        ],
        [
            "7000",
            "8000",
            "9000",
        ],
        [
            "10000",
        ],
    ]
    example_results = 24000
    assert solution_1(example_input) == example_results
    print("Tests 1 successful")


def test_solution_2():
    example_input = [
        [
            "1000",
            "2000",
            "3000",
        ],
        [
            "4000",
        ],
        [
            "5000",
            "6000",
        ],
        [
            "7000",
            "8000",
            "9000",
        ],
        [
            "10000",
        ],
    ]
    example_result = 45000
    assert solution_2(example_input) == example_result
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
