def load_input(path):
    lines = []
    with open(path) as f:
        for line in f:
            lines.append(line.rstrip())

    return lines


def line_checker(line):
    expected_close = []
    valid_brackets = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]
    for char in line:
        char_is_invalid = True
        for open_bracket, close_bracket in valid_brackets:
            if char == open_bracket:
                expected_close.append(close_bracket)
                char_is_invalid = False
                break
        if char_is_invalid:
            next_close = expected_close.pop()
            if next_close != char:
                return char

    return expected_close


def syntax_error_score(nav_lines):
    error_sum = 0
    for line in nav_lines:
        invalid_char = line_checker(line)
        if invalid_char == ")":
            error_sum += 3
        elif invalid_char == "]":
            error_sum += 57
        elif invalid_char == "}":
            error_sum += 1197
        elif invalid_char == ">":
            error_sum += 25137

    return error_sum


def median_completion_score(nav_lines):
    line_scores = []
    close_bracket = [")", "]", "}", ">"]
    for line in nav_lines:
        checker_return = line_checker(line)
        if type(checker_return) is list:
            line_score = 0
            checker_return.reverse()
            for char in checker_return:
                line_score *= 5
                for i, bracket in enumerate(close_bracket):
                    if char == bracket:
                        line_score += i + 1

            line_scores.append(line_score)
    line_scores.sort()
    return line_scores[len(line_scores) // 2]


nav_lines = load_input("2021/inputs/day10.txt")
print(f"The syntax error score is: {syntax_error_score(nav_lines)}")
print(f"The median string comletion score is: {median_completion_score(nav_lines)}")
