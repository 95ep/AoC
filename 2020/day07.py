import re


def process_rules(path):
    rules_dict = {}
    with open(path) as f:
        for line in f:
            exp_parent_bag = re.compile(r"(.+) bags contain (.+ bags?).\n?")
            exp_child_bags = re.compile(r"(\d) (.+) bags?")
            parent_bag, children_str = re.match(exp_parent_bag, line).groups()

            child_bags = []

            if children_str != "no other bags":
                child_list = children_str.split(', ')
                for child_str in child_list:
                    number, child = re.match(exp_child_bags, child_str).groups()
                    child_bags.append((child, int(number)))

            rules_dict[parent_bag] = child_bags

    return rules_dict


def can_contain_check(parent, desired_child, rules):
    allowed_children = rules[parent]
    for allowed_child, numb in allowed_children:
        if allowed_child == desired_child:
            return True
        elif can_contain_check(allowed_child, desired_child, rules):
            return True

    return False


def sum_possible_parents(rules, desired_child):
    n_possible = 0
    for key in rules:
        if key != desired_child and can_contain_check(key, desired_child, rules):
            n_possible += 1

    return n_possible


def number_child_bags(parent_bag, rules):
    n_children = 1
    for child, value in rules[parent_bag]:
        n_children += value * number_child_bags(child, rules)

    return n_children


rules = process_rules('inputs/day07.txt')
print(f"Part 1 - number of possible outer bags: {sum_possible_parents(rules, 'shiny gold')}")
# Must subtract outer most bag from the answer
print(f"Part 2 - number of inner bags: {number_child_bags('shiny gold', rules) - 1}")