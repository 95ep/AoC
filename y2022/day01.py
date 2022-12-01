from utils.readers import reader_split_by_exp


def calc_calories_per_elf(input):
    calories_per_elf = []
    for inventory in input:
        cumulative_calories = 0
        for item in inventory:
            cumulative_calories += int(item)
        calories_per_elf.append(cumulative_calories)
    return calories_per_elf


def solution_1(input):
    calories_per_elf = calc_calories_per_elf(input)

    return max(calories_per_elf)


def solution_2(input):
    calories_per_elf = calc_calories_per_elf(input)
    top_three = sorted(calories_per_elf)[-3:]
    return sum(top_three)


if __name__ == "__main__":
    input = reader_split_by_exp("y2022/inputs/day01.txt", "$")
    print(f"Answer to part 1 is: {solution_1(input)}")
    print(f"Answer to part 2 is: {solution_2(input)}")
