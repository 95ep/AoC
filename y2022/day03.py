from utils.readers import reader_split_by_line


def extract_rucksack_contents(puzzle_input):
    content = []
    for rucksack_str in puzzle_input:
        n_items = len(rucksack_str)
        items_1 = rucksack_str[: n_items // 2]
        items_2 = rucksack_str[n_items // 2 :]
        content.append((items_1, items_2))

    return content


def find_duplicated_types(rucksack_contents):
    duplicated_types = []
    for content in rucksack_contents:
        for type in content[0]:
            if type in content[1]:
                duplicated_types.append(type)
                break

    return duplicated_types


def find_badge_types(rucksack_contents):
    badge_types = []
    for idx in range(0, len(rucksack_contents), 3):
        for item_type in rucksack_contents[idx]:
            if (
                item_type in rucksack_contents[idx + 1]
                and item_type in rucksack_contents[idx + 2]
            ):
                badge_types.append(item_type)
                break
    return badge_types


def summarize_priority(types):
    sum_prio = 0
    for item_type in types:
        if item_type.isupper():
            item_type = item_type.lower()
            sum_prio += 26
        sum_prio += ord(item_type) - ord("a") + 1

    return sum_prio


def solution_1(input_path):
    puzzle_input = reader_split_by_line(input_path)
    rucksack_contents = extract_rucksack_contents(puzzle_input)
    duplicated_types = find_duplicated_types(rucksack_contents)
    return summarize_priority(duplicated_types)


def solution_2(input_path):
    puzzle_input = reader_split_by_line(input_path)
    badge_types = find_badge_types(puzzle_input)
    return summarize_priority(badge_types)


if __name__ == "__main__":
    input_path = "y2022/inputs/day03.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
