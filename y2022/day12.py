import numpy as np

from utils.readers import reader_split_by_line
from utils.priority_queue import PriorityQueue

NEIGHBOUR_COORDS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def dijkstras(source, graph):
    dist = np.ones(graph.shape[:2], dtype=np.int32) * np.iinfo(np.int32).max - 1
    dist[source] = 0
    pq = PriorityQueue()

    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            pq.add_with_priority((i, j), dist[i, j])

    while 1 == 1:
        u = pq.pop()
        if u is None:
            return dist
        for idx, is_neighbour in enumerate(graph[u]):
            if is_neighbour:
                alt_dist = dist[u] + 1
                delta_i, delta_j = NEIGHBOUR_COORDS[idx]
                v = (u[0] + delta_i, u[1] + delta_j)
                if alt_dist < dist[v]:
                    dist[v] = alt_dist
                    pq.change_priority(v, alt_dist)


def find_start_and_endpoint(raw_input):
    for i in range(len(raw_input)):
        for j in range(len(raw_input[0])):
            if raw_input[i][j] == "S":
                start = (i, j)
                raw_input[i] = raw_input[i].replace("S", "a")
            elif raw_input[i][j] == "E":
                end = (i, j)
                raw_input[i] = raw_input[i].replace("E", "z")
    return start, end


def find_all_coords_for_level(raw_input, level):
    coords = []
    for i in range(len(raw_input)):
        for j in range(len(raw_input[0])):
            if raw_input[i][j] == level:
                coords.append((i, j))
    return coords


def build_graph(raw_input):
    # Build graph in "reverse" direction to support distance from arbitrary start point
    graph = np.zeros(shape=(len(raw_input), len(raw_input[0]), 4), dtype=np.bool8)
    for i in range(len(raw_input)):
        for j in range(len(raw_input[0])):
            h = ord(raw_input[i][j])
            # iterate over neighbours
            for k, (delta_i, delta_j) in enumerate(NEIGHBOUR_COORDS):
                i_tilde = i + delta_i
                j_tilde = j + delta_j
                if (
                    i_tilde > -1
                    and i_tilde < graph.shape[0]
                    and j_tilde > -1
                    and j_tilde < graph.shape[1]
                ):
                    if h - ord(raw_input[i_tilde][j_tilde]) < 2:
                        graph[i, j, k] = True

    return graph


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    start, end = find_start_and_endpoint(inp)
    graph = build_graph(inp)
    dist_matrix = dijkstras(end, graph)
    return dist_matrix[start]


def solution_2(input_path):
    inp = reader_split_by_line(input_path)
    _, end = find_start_and_endpoint(inp)
    all_a_coords = find_all_coords_for_level(inp, "a")
    graph = build_graph(inp)
    dist_matrix = dijkstras(end, graph)
    shortest_path = [dist_matrix[start] for start in all_a_coords]

    return min(shortest_path)


if __name__ == "__main__":
    input_path = "y2022/inputs/day12.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
