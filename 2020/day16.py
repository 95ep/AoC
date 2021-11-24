import re


def load_input(path):
    rule_pattern = re.compile(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)\n")
    values_pattern = re.compile(r"\d+")
    rules = {}
    tickets_list = []
    with open(path) as f:
        for line in f:
           if line == '\n':
               f.readline()
               break

           field, bound1, bound2, bound3, bound4 = re.match(rule_pattern, line).groups()
           rules[field] = (int(bound1), int(bound2), int(bound3), int(bound4))

        my_ticket = [int(v) for v in re.findall(values_pattern, f.readline())]
        f.readline()
        f.readline()

        for line in f:
            values = re.findall(values_pattern, line)
            tickets_list.append([int(v) for v in values])

    return rules, my_ticket, tickets_list


def calc_error_rate(rules, tickets):
    error_rate = 0
    for ticket in tickets:
        error_rate += check_valid(ticket, rules)

    return error_rate


def check_valid(ticket, rules):
    invalid_sum = 0
    for val in ticket:
        is_valid = False
        for rule in rules.values():
            if (rule[0] <= val and val <= rule[1]) or (rule[2] <= val and val <= rule[3]):
                is_valid = True

        if not is_valid:
            invalid_sum += val

    return invalid_sum

def check_valid2(ticket, rules):
    for val in ticket:
        is_valid = False
        for rule in rules.values():
            if (rule[0] <= val and val <= rule[1]) or (rule[2] <= val and val <= rule[3]):
                is_valid = True

        if not is_valid:
            return False

    return True


def remove_invalid(tickets, rules):
    valid_tickets = []
    for ticket in tickets:
        if check_valid2(ticket, rules):
            valid_tickets.append(ticket)

    return valid_tickets


def values_per_field(tickets):
    vals_per_field = [[] for _ in range(len(tickets[0]))]
    for ticket in tickets:
        for field, val in enumerate(ticket):
            vals_per_field[field].append(val)

    return vals_per_field

def is_matching_rule(values, rule):
    for val in values:
        if not ((rule[0] <= val and val <= rule[1]) or (rule[2] <= val and val <= rule[3])):
            return False

    return True

def get_potential_fields(tickets, rules):
    valid_tickets = remove_invalid(tickets, rules)
    matching_fields = []
    vals_per_field = values_per_field(valid_tickets)
    for values in vals_per_field:
        fields = []
        for field in rules:
            if is_matching_rule(values, rules[field]):
                fields.append(field)
        matching_fields.append(fields)

    return matching_fields


def assign_field_names(potential_fields):
    correct_fields = ['' for _ in range(len(potential_fields))]
    for _ in range(len(potential_fields)):
        for idx, fields in enumerate(potential_fields):
            if len(fields) == 1:
                locked_field = fields[0]
                correct_fields[idx] = locked_field
                break

        for fields in potential_fields:
            if locked_field in fields:
                fields.remove(locked_field)

    return correct_fields

def calc_task2_product(correct_fields, my_ticket):
    prod = 1
    for idx, field in enumerate(correct_fields):
        if len(re.findall("departure", field)) > 0:
            prod *= my_ticket[idx]

    return prod


rules, my_ticket, tickets = load_input('inputs/day16.txt')

print(f"The scanning error rate is: {calc_error_rate(rules, tickets)}")
possible_fields = get_potential_fields(tickets, rules)
correct_fields = assign_field_names(possible_fields)
print(calc_task2_product(correct_fields, my_ticket))
