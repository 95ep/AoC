from math import ceil, floor


def load_input(path):
    with open(path) as f:
        return [int(p) for p in f.readline().split(",")]


def calc_fule_for_move(positions, desired_position):
    fuel_cost = 0
    for p in positions:
        fuel_cost += abs(desired_position - p)

    return fuel_cost


def find_cheapest_move(positions):
    positions.sort()
    if len(positions) % 2 == 0:
        median_idx = len(positions) // 2
        return calc_fule_for_move(positions, positions[median_idx])
    else:
        idx_1 = len(positions) // 2
        idx_2 = idx_1 + 1
        return (
            calc_fule_for_move(positions, idx_1) + calc_fule_for_move(positions, idx_2)
        ) / 2


def calc_fule_for_move_v2(positions, desired_position):
    fuel_cost = 0
    for p in positions:
        distance = abs(desired_position - p)
        if distance == 1:
            fuel_cost += 1
        else:
            fuel_cost += distance * (1 + distance) // 2

    return fuel_cost


def find_cheapest_move_v2(positions):
    floored = floor(sum(positions) // len(positions))
    ceiled = ceil(sum(positions) // len(positions))

    cost_floored = calc_fule_for_move_v2(positions, floored)
    cost_ceiled = calc_fule_for_move_v2(positions, ceiled)
    if cost_floored < cost_ceiled:
        return cost_floored
    else:
        return cost_ceiled


positions = load_input("2021/inputs/day07.txt")
print(f"Cheapest move part 1: {find_cheapest_move(positions)}")
print(f"Cheapest move part 2: {find_cheapest_move_v2(positions)}")
