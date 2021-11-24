def load_input(path):
    all_groups = []
    tmp_group = []
    with open(path) as f:
        for line in f:
            if line == '\n':
                all_groups.append(tmp_group)
                tmp_group = []
            else:
                tmp_group.append(line.strip('\n'))
        all_groups.append(tmp_group)
    return all_groups


def count_unique(group):
    n_unique = 0
    checked_answers = []
    for answer in group:
        for char in answer:
            if char not in checked_answers:
                n_unique += 1
                checked_answers.append(char)

    return n_unique


def count_common(group):
    if len(group) == 1:
        return len(group[0])
    else:
        n_common = 0
        for char in group[0]:
            common = True
            for idx in range(1, len(group)):
                if char not in group[idx]:
                    common = False
                    break

            if common:
                n_common += 1

        return n_common

groups = load_input('inputs/day06.txt')
print(f"Sum of unique answers: {sum([count_unique(g) for g in groups])}")
print(f"Sum of common answers: {sum([count_common(g) for g in groups])}")