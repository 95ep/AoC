from y2021.day16 import solution_1


def test_solution_1():
    example_inputs = [
        "8A004A801A8002F478",
        "620080001611562C8802118E34",
        "C0015000016115A2E0802F182340",
        "A0016C880162017C3686B18A3D4780",
    ]
    example_results = [16, 12, 23, 31]
    for input, result in zip(example_inputs, example_results):
        assert solution_1(input) == result

    print("Tests successful")


if __name__ == "__main__":
    test_solution_1()
