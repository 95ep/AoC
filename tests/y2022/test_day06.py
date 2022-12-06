import time
from y2022.day06 import solution_1, solution_2


def test_solution_1():
    example_input_files = [
        "day06-0.txt",
        "day06-1.txt",
        "day06-2.txt",
        "day06-3.txt",
        "day06-4.txt",
    ]
    example_results = [7, 5, 6, 10, 11]
    for file_name, result in zip(example_input_files, example_results):
        assert solution_1("tests/y2022/inputs/" + file_name) == result
    print("Tests 1 successful")


def test_solution_2():
    example_input_files = [
        "day06-0.txt",
        "day06-1.txt",
        "day06-2.txt",
        "day06-3.txt",
        "day06-4.txt",
    ]
    example_results = [19, 23, 23, 29, 26]
    for file_name, result in zip(example_input_files, example_results):
        assert solution_2("tests/y2022/inputs/" + file_name) == result
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
