from y2021.day16 import solution_1, solution_2


def test_solution_1():
    example_inputs = [
        "D2FE28",
        "38006F45291200",
        "8A004A801A8002F478",
        "EE00D40C823060",
        "620080001611562C8802118E34",
        "C0015000016115A2E0802F182340",
        "A0016C880162017C3686B18A3D4780",
    ]
    example_results = [6, 9, 16, 14, 12, 23, 31]
    for input, result in zip(example_inputs, example_results):
        assert solution_1(input) == result

    print("Tests 1 successful")


def test_solution_2():
    example_inputs = [
        "C200B40A82",
        "04005AC33890",
        "880086C3E88112",
        "CE00C43D881120",
        "D8005AC2A8F0",
        "F600BC2D8F",
        "9C005AC2F8F0",
        "9C0141080250320F1802104A08",
    ]
    example_results = [3, 54, 7, 9, 1, 0, 0, 1]
    for input, result in zip(example_inputs, example_results):
        assert solution_2(input) == result

    print("Tests 2 successful")


if __name__ == "__main__":
    test_solution_1()
    test_solution_2()
