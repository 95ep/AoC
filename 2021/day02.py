def read_input(path):
    instructions = []
    with open(path) as f:
        for line in f:
            tmp = line.split()
            instructions.append((tmp[0], int(tmp[1])))

    return instructions


def calc_position(instructions):
    x = 0
    y = 0
    for operation, distance in instructions:
        if operation == "forward":
            x += distance
        elif operation == "down":
            y += distance
        else:
            y -= distance

    return x, y


def calc_position_v2(instructions):
    x = 0
    y = 0
    aim = 0
    for operation, distance in instructions:
        if operation == "forward":
            x += distance
            y += distance * aim
        elif operation == "down":
            aim += distance
        else:
            aim -= distance

    return x, y


instructions = read_input("2021/inputs/day02.txt")
x, y = calc_position(instructions)
print(f"Horizontal position is: {x} and depth is {y}. Their product is {x*y}")
x, y = calc_position_v2(instructions)
print(
    "According to part 2 logic: Horizontal position is:"
    f"{x} and depth is {y}. Their product is {x*y}"
)
