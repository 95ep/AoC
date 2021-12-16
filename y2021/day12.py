def load_input(path):
    node_connections = {}
    with open(path) as f:
        for line in f:
            node_1, node_2 = line.rstrip().split("-")
            nodes = [(node_1, node_2), (node_2, node_1)]
            for n1, n2 in nodes:
                if n1 not in node_connections:
                    node_connections[n1] = [n2]
                else:
                    node_connections[n1].append(n2)

    return node_connections


def find_paths(node_connections):
    path_queue = [["start"]]
    valid_paths = []
    while len(path_queue) > 0:
        p = path_queue.pop()
        for next_node in node_connections[p[-1]]:
            if next_node == "end":
                new_p = [*p, next_node]
                valid_paths.append(new_p)
            else:
                if next_node.islower() and next_node in p:
                    continue
                # If big cave or first time in small
                new_p = [*p, next_node]
                path_queue.append(new_p)

    return len(valid_paths)


def double_cave_in_path(p):
    small_cave_list = [c for c in p if c.islower()]
    unique_list = []
    for cave in small_cave_list:
        if cave not in unique_list:
            unique_list.append(cave)
        else:
            return True

    return False


def find_paths_v2(node_connections):
    path_queue = [["start"]]
    valid_paths = []
    while len(path_queue) > 0:
        p = path_queue.pop()
        for next_node in node_connections[p[-1]]:
            if next_node == "end":
                new_p = [*p, next_node]
                valid_paths.append(new_p)
            elif next_node == "start":
                continue
            else:
                if next_node.islower() and next_node in p:
                    if double_cave_in_path(p):
                        continue
                # If big cave or first time in small
                new_p = [*p, next_node]
                path_queue.append(new_p)

    return len(valid_paths)


connections = load_input("2021/inputs/day12.txt")
print(f"n paths according to part 1 rules: {find_paths(connections)}")
print(f"n path according to part 2 rules: {find_paths_v2(connections)}")
