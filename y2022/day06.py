from utils.readers import reader_split_by_line


def find_marker(input_string, marker_size):
    last_four = [input_string[i] for i in range(marker_size - 1)]
    for i in range(3, len(input_string)):
        last_four.append(input_string[i])
        if len(set(last_four)) == marker_size:
            return i + 1
        last_four.pop(0)


def solution_1(input_path):
    inp = reader_split_by_line(input_path)[0]
    return find_marker(inp, 4)


def solution_2(input_path):
    inp = reader_split_by_line(input_path)[0]
    return find_marker(inp, 14)


if __name__ == "__main__":
    input_path = "y2022/inputs/day06.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
