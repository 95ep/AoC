import time
import numpy as np

from utils.priority_queue import PriorityQueue


def load_input(path):
    risk_map = []
    with open(path) as f:
        for line in f:
            risk_map.append([int(i) for i in line.rstrip()])

    return np.array(risk_map, dtype=int)


def build_graph(risk_map):
    n_rows = len(risk_map)
    n_columns = len(risk_map[0])
    graph = []
    for i1, row in enumerate(risk_map):
        for i2, _ in enumerate(row):
            neighbours = []
            potential_neighbours = [
                (i1, i2 + 1),
                (i1, i2 - 1),
                (i1 + 1, i2),
                (i1 - 1, i2),
            ]
            for idx1, idx2 in potential_neighbours:
                if idx1 > -1 and idx2 > -1 and idx1 < n_rows and idx2 < n_columns:
                    # Add node idx and risk
                    neighbours.append((idx1 * n_rows + idx2, risk_map[idx1][idx2]))

            graph.append(neighbours)

    return graph


def dijkstras(graph):
    # Some very large int as stand in for inf
    dist = [999999999 for _ in range(len(graph))]
    dist[0] = 0
    prev = [None for _ in range(len(graph))]
    queue = PriorityQueue()
    for node, d in enumerate(dist):
        queue.add_with_priority(node, d)

    target = len(graph) - 1

    while len(queue) > 0:
        # Find node with lowest dist in queue
        next_node = queue.pop()

        # Check if reached target node
        if next_node == target:
            break

        # Iterate over neighbours to queue
        for neighbour, risk in graph[next_node]:
            alt_dist = dist[next_node] + risk
            if dist[neighbour] is None or alt_dist < dist[neighbour]:
                dist[neighbour] = alt_dist
                prev[neighbour] = next_node
                queue.change_priority(neighbour, alt_dist)

    return dist[-1]


def extend_map(map):
    rows, cols = map.shape
    extended_map = np.zeros((rows * 5, cols * 5), dtype=int)
    for i1 in range(5):
        for i2 in range(5):
            extended_map[i1 * rows : (i1 + 1) * rows, i2 * cols : (i2 + 1) * cols] = (
                map + i1 + i2
            )

    extended_map[extended_map > 9] = extended_map[extended_map > 9] % 9
    return extended_map


risk_map = load_input("2021/inputs/day15.txt")

ts = time.time()
graph = build_graph(risk_map)
print(f"Lowest risk for path through part 1 map is: {dijkstras(graph)}")
print(f"Calculating part 1 answer took {time.time()-ts} seconds")

ts = time.time()
extended_map = extend_map(risk_map)
extended_graph = build_graph(extended_map)
print(f"Lowest risk for path through part 2 map is: {dijkstras(extended_graph)}")
print(f"Calculating part 2 answer took {time.time()-ts} seconds")
