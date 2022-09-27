from time import perf_counter

from utils.readers import reader_split_by_line
from utils.priority_queue import PriorityQueue

POD_TO_ROOM_MAP = {"A": 0, "B": 1, "C": 2, "D": 3}
POD_TO_ENERGY_MAP = {"A": 1, "B": 10, "C": 100, "D": 1000}


def calc_cost_to_hall(room, room_cell, current_state):
    # Check cells on the way to hall, excluding moving pod cell
    to_hall_path = [
        current_state[cell_idx]
        for cell_idx in range(11 + room, 11 + room + 4 * room_cell, 4)
    ]
    # Append enter hall cell
    to_hall_path.append(current_state[2 + room * 2])

    # Check that the way is clear
    for cell in to_hall_path:
        if cell != ".":
            return None

    return room_cell + 1


def calc_cost_in_hall(enter_hall_cell, target_cell, current_state):
    if enter_hall_cell == target_cell:
        # Corresponds to moving back into the same room pod is
        # trying to leave
        return None

    if enter_hall_cell < target_cell:
        visited_cells = current_state[enter_hall_cell + 1 : target_cell + 1]
    else:
        visited_cells = current_state[target_cell:enter_hall_cell]
    for cell in visited_cells:
        if cell != ".":
            return None

    return len(visited_cells)


def find_moves_to_hall(start_cell, enter_hall_cell, current_state, pod, cost_to_hall):
    valid_moves = []
    valid_target_cells = [0, 1, 3, 5, 7, 9, 10]
    for target_cell in valid_target_cells:
        cost_in_hall = calc_cost_in_hall(enter_hall_cell, target_cell, current_state)
        if cost_in_hall is None:
            continue

        cost = (cost_to_hall + cost_in_hall) * POD_TO_ENERGY_MAP[pod]
        valid_moves.append(((start_cell, target_cell), cost))

    return valid_moves


def find_move_to_room(start_cell, enter_hall_cell, current_state, pod, cost_to_hall):
    target_room = POD_TO_ROOM_MAP[pod]

    exit_hall_cell = 2 + target_room * 2
    cost_in_hall = calc_cost_in_hall(enter_hall_cell, exit_hall_cell, current_state)
    if cost_in_hall is None:  # Path in hallway is blocked
        return []

    room_cell_idx = [idx for idx in range(11 + target_room, len(current_state), 4)]
    room_cells = [current_state[cell_idx] for cell_idx in room_cell_idx]

    # Check only correct pod types in room
    for cell in room_cells:
        if cell != pod and cell != ".":
            return []

    if pod not in room_cells:
        # Rooms is empty
        room_cell = len(room_cells) - 1
    else:
        room_cell = room_cells.index(pod) - 1
    target_cell = room_cell_idx[room_cell]
    cost = (cost_to_hall + cost_in_hall + room_cell + 1) * POD_TO_ENERGY_MAP[pod]

    return [((start_cell, target_cell), cost)]


def is_in_correct_position(room, room_cell, pod, current_state):
    correct_room = POD_TO_ROOM_MAP[pod]
    if room != correct_room:
        return False

    pod_and_blocked_cells = [
        current_state[cell_idx]
        for cell_idx in range(11 + room + 4 * room_cell, len(current_state), 4)
    ]
    # Check that cells have the right pod type
    for cell in pod_and_blocked_cells:
        if cell != pod:
            return False
    return True


def find_valid_moves(current_state):
    # Moves starting in rooms
    moves_to_hall = []
    moves_to_room = []
    n_room_cells = (len(current_state) - 11) // 4
    for room in range(4):
        for room_cell in range(n_room_cells):
            start_cell = 11 + room_cell * 4 + room
            pod = current_state[start_cell]
            if pod == ".":
                continue
            if is_in_correct_position(room, room_cell, pod, current_state):
                continue

            cost_to_hall = calc_cost_to_hall(room, room_cell, current_state)

            if cost_to_hall is None:  # If another pod is blocking the exit
                continue

            enter_hall_cell = 2 + room * 2
            moves_to_hall.extend(
                find_moves_to_hall(
                    start_cell, enter_hall_cell, current_state, pod, cost_to_hall
                )
            )
            moves_to_room.extend(
                find_move_to_room(
                    start_cell, enter_hall_cell, current_state, pod, cost_to_hall
                )
            )

    # Moves starting in hallway
    moves_from_hall_to_room = []
    for start_cell in range(11):
        pod = current_state[start_cell]
        if pod == ".":
            continue
        moves_from_hall_to_room.extend(
            find_move_to_room(start_cell, start_cell, current_state, pod, 0)
        )

    return [*moves_to_hall, *moves_to_room, *moves_from_hall_to_room]


def get_neighbour_states(current_state):
    valid_moves = find_valid_moves(current_state)
    neighbour_states = []
    for move, energy in valid_moves:
        # Move amphipod from src to target
        new_state_list = list(current_state)
        new_state_list[move[1]] = new_state_list[move[0]]
        new_state_list[move[0]] = "."
        new_state = "".join(new_state_list)
        neighbour_states.append((new_state, energy))

    return neighbour_states


def find_lowest_energy(initial_state, target_state):
    queue = PriorityQueue()
    queue.add_with_priority((initial_state, 0), 0)
    while len(queue.pq) > 0:
        current_state, current_energy = queue.pop()
        # Check if current state matches desired state
        if current_state == target_state:
            return current_energy
        # Get all states possible by moving one amphipod
        neighbour_states = get_neighbour_states(current_state)
        # Add all neighbour states to the queue
        for state, move_energy in neighbour_states:
            energy_consumed = current_energy + move_energy
            item = (state, energy_consumed)
            if not queue.is_in_queue(item):
                queue.add_with_priority((state, energy_consumed), energy_consumed)


def solution_1(input):
    initial_state = "..........." + input[2][3:10:2] + input[3][1:8:2]
    target_state = "...........ABCDABCD"

    return find_lowest_energy(initial_state, target_state)


def solution_2(input):
    initial_state_lines = ["...........", input[2], "DCBA", "DBAC", input[3]]
    initial_state = ""
    for input_line in initial_state_lines:
        initial_state = initial_state + input_line

    initial_state = initial_state.replace("#", "")
    target_state = "...........ABCDABCDABCDABCD"

    return find_lowest_energy(initial_state, target_state)


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day23.txt")
    tic = perf_counter()
    answer_1 = solution_1(input)
    print(f"Answer to part 1 is: {answer_1}. Obtained in {perf_counter()-tic} s.")

    tic = perf_counter()
    answer_2 = solution_2(input)
    print(f"Answer to part 2 is: {answer_2}. Obtained in {perf_counter()-tic} s.")
