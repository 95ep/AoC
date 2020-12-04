import re


def load_input(path):
    entries = []
    with open(path) as f:
        entry = ''
        for line in f:
            if line == '\n':
                entries.append(entry)
                entry = ''
            else:
                entry += line

    entries.append(entry)
    return entries

def check_fields(expected_fields, data_list):
    n_valid = 0
    for entry in data_list:
        valid = True
        for field in expected_fields:
            if entry.find(field) == -1:
                valid = False
                break

        if valid:
            n_valid += 1

    return n_valid

def check_fields_strict(data_list):
    n_valid = 0
    for entry in data_list:
        # Check byr
        match = re.match(r".*byr:(\d{4})[ \n].*", entry, re.DOTALL)
        if match is None:
            continue
        else:
            byr = int(match.groups()[0])
        if byr < 1920 or byr > 2002:
            continue

        # Check iyr
        match = re.match(r".*iyr:(\d{4})[ \n].*", entry, re.DOTALL)
        if match is None:
            continue
        else:
            iyr = int(match.groups()[0])
        if iyr < 2010 or iyr > 2020:
            continue

        # Check eyr
        match = re.match(r".*eyr:(\d{4})[ \n].*", entry, re.DOTALL)
        if match is None:
            continue
        else:
            eyr = int(match.groups()[0])
        if eyr < 2020 or eyr > 2030:
            continue

        # Check hgt
        match = re.match(r".*hgt:(\d*)(cm|in)[ \n].*", entry, re.DOTALL)
        if match is None:
            continue
        else:
            groups = match.groups()
            hgt, unit = int(groups[0]), groups[1]
            if unit == 'in'  and (hgt < 59 or hgt > 76):
                continue
            elif unit == 'cm'  and (hgt < 150 or hgt > 193):
                continue

        # Check hcl
        match = re.match(r".*hcl:#([0-9a-f]{6})[ \n].*", entry, re.DOTALL)

        if match is None:
            continue

        # Check ecl
        match = re.match(r".*ecl:(amb|blu|brn|gry|grn|hzl|oth)[ \n].*", entry, re.DOTALL)

        if match is None:
            continue

        # Check pid
        match = re.match(r".*pid:(\d{9})[ \n].*", entry, re.DOTALL)
        if match is None:
            continue

        n_valid += 1

    return n_valid


# Task one
passport_data = load_input('inputs/day04.txt')
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
print(f"Solution to task one {check_fields(fields, passport_data)}.")
print(f"Solution to task two {check_fields_strict(passport_data)}.")
