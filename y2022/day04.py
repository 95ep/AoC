from utils.readers import reader_split_by_line


def extract_assignment_pairs(assignment_strs):
    assignments = []
    for assignment_pairs in assignment_strs:
        individual_str = assignment_pairs.split(",")
        assignment_1 = [int(val) for val in individual_str[0].split("-")]
        assignment_2 = [int(val) for val in individual_str[1].split("-")]
        assignments.append((assignment_1, assignment_2))

    return assignments


def count_full_overlap(assignments):
    n_overlaps = 0
    for assignment_pair in assignments:
        if (
            assignment_pair[0][0] <= assignment_pair[1][0]
            and assignment_pair[0][1] >= assignment_pair[1][1]
        ):
            n_overlaps += 1
        elif (
            assignment_pair[0][0] >= assignment_pair[1][0]
            and assignment_pair[0][1] <= assignment_pair[1][1]
        ):
            n_overlaps += 1

    return n_overlaps


def count_partial_overlap(assignments):
    n_overlaps = 0
    for assignment_pair in assignments:
        if (
            assignment_pair[0][0] <= assignment_pair[1][1]
            and assignment_pair[0][1] >= assignment_pair[1][0]
        ):
            n_overlaps += 1

    return n_overlaps


def solution_1(input_path):
    assignment_strs = reader_split_by_line(input_path)
    assignments = extract_assignment_pairs(assignment_strs)
    return count_full_overlap(assignments)


def solution_2(input_path):
    assignment_strs = reader_split_by_line(input_path)
    assignments = extract_assignment_pairs(assignment_strs)
    return count_partial_overlap(assignments)


if __name__ == "__main__":
    input_path = "y2022/inputs/day04.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
