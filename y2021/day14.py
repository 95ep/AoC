from functools import lru_cache
import re


def load_input(path):
    with open(path) as f:
        polymer = f.readline().rstrip()

        # Flush blank line
        f.readline()
        rules = {}
        p = re.compile(r"(\S\S) -> (\S)")
        for line in f:
            m = re.search(p, line)
            pair, insertion = m.groups()
            rules[pair] = insertion

    return polymer, rules


def grow_polymer(polymer, rules, n_cycles):
    pairs_dict = {}
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        if pair in pairs_dict:
            pairs_dict[pair] += 1
        else:
            pairs_dict[pair] = 1

    for _ in range(n_cycles):
        new_pairs_dict = {}
        for pair, occs in pairs_dict.items():
            new_element = rules[pair]
            new_pairs = [pair[0] + new_element, new_element + pair[1]]
            for new_pair in new_pairs:
                if new_pair in new_pairs_dict:
                    new_pairs_dict[new_pair] += occs
                else:
                    new_pairs_dict[new_pair] = occs

        pairs_dict = new_pairs_dict

    # Calc score
    element_occs = {}
    for pair, occs in pairs_dict.items():
        for element in pair:
            if element in element_occs:
                element_occs[element] += occs
            else:
                element_occs[element] = occs

    # Adjust for edges and double counting
    element_occs[polymer[0]] += 1
    element_occs[polymer[-1]] += 1

    for element, occs in element_occs.items():
        element_occs[element] = occs // 2

    return max(element_occs.values()) - min(element_occs.values())


starting_polymer, rules = load_input("2021/inputs/day14.txt")
# Part 1
score_1 = grow_polymer(starting_polymer, rules, 10)
print(f"The score for the part 1 polymer is {score_1}")

# Part 2
score_2 = grow_polymer(starting_polymer, rules, 40)
print(f"The score for the part 2 polymer is {score_2}")
