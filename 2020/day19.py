from itertools import product
import re

def load_input(path):
    rules_dict = {}
    with open(path) as f:
        rule_pattern = re.compile(r"(\d+): (.*)")
        m = re.match(rule_pattern, f.readline())
        while m:
            rule_num = m.group(1)
            rule_str = m.group(2)
            if rule_str.find('|') != -1:
                rules_list = rule_str.split('|')
            else:
                rules_list = [rule_str]

            tmp_list = []

            for rule in rules_list:
                rule_match = re.findall(r"(\d+)", rule)
                if len(rule_match) == 0:
                    rule_match = re.findall(r'"."', rule)
                tmp_list.append(rule_match)
            rules_dict[rule_num] = tmp_list

            m = re.match(rule_pattern, f.readline())

        messages = [line.strip('\n') for line in f]

        return rules_dict, messages


def form_matches(rule, rules_dict):
    char_patter = r'"(.)"'
    all_patterns = []
    for sub_rule in rule:
        child_patterns = []
        for instruction in sub_rule:
            if re.match(char_patter, instruction):
                child_patterns.append(re.match(char_patter, instruction).group(1))
            else:
                child_patterns.append(form_matches(rules_dict[instruction], rules_dict))


        # Combine all in child patterns
        pattern_combs = product(*child_patterns)
        for comb in pattern_combs:
            s_tmp = ''
            for s in comb:
                s_tmp += s
            all_patterns.append(s_tmp)

    return all_patterns

def match_messages(valid_patterns, messages):
    n_valid = 0
    for message in messages:
        if message in valid_patterns:
            n_valid += 1

    return n_valid

rules, messages = load_input('inputs/day19.txt')

all_patterns = form_matches(rules['0'], rules)
print(f"Number of valid messages are {match_messages(all_patterns, messages)}")