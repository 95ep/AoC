from time import perf_counter as pfc

from utils.readers import reader_split_by_line

### pseudo code for the ALU program block
# def block_program(lq, add_to_x, add_to_y, divide_z_by):
#     # divide_z_by is always 1 or 26
#     # divide by 26 always followed by large-ish negative
#     # add_to_y -> only chance to skip pushing to stack
#     # stack must be empty at end of program -> 7 pop and
#     # 7 push needed
#     w = next_digit()
#     if len(lq) > 0:
#         a = lq[-1]
#     else:
#         a = 0
#     if divide_z_by == 26:
#         lq.pop()
#     if a + add_to_x != w:
#         lq.append(w + add_to_y)

#     return lq


def extract_relevant_variables(input):
    add_to_x, add_to_y, divide_z_by = [], [], []
    for i in range(0, len(input), 18):
        add_to_x.append(int(input[i + 5].split()[2]))
        add_to_y.append(int(input[i + 15].split()[2]))
        divide_z_by.append(int(input[i + 4].split()[2]))

    return add_to_x, add_to_y, divide_z_by


def get_model_no(add_to_x, add_to_y, divide_z_by, part_1=True):
    stack = []
    model_no = [0 for _ in range(14)]
    for i, (u, v, w) in enumerate(zip(add_to_x, add_to_y, divide_z_by)):
        if w == 1:
            stack.append((i, v))
        else:
            iv, v_tilde = stack.pop()
            # relation between digits and params is:
            # model_no[iv] + v_tilde + u == model_no[i]
            param_sum = v_tilde + u
            if part_1:
                model_no[iv] = min(9, 9 - param_sum)
                model_no[i] = model_no[iv] + param_sum
            else:
                model_no[iv] = max(1, 1 - param_sum)
                model_no[i] = model_no[iv] + param_sum

    return "".join([str(digit) for digit in model_no])


def solution_1(input):
    add_to_x, add_to_y, divide_z_by = extract_relevant_variables(input)
    return get_model_no(add_to_x, add_to_y, divide_z_by)


def solution_2(input):
    add_to_x, add_to_y, divide_z_by = extract_relevant_variables(input)
    return get_model_no(add_to_x, add_to_y, divide_z_by, False)


if __name__ == "__main__":
    input = reader_split_by_line("y2021/inputs/day24.txt")
    tic = pfc()
    answer_1 = solution_1(input)
    print(
        "Answer to part 1 is: '{}'. Obtained in {:.2f} ms.".format(
            answer_1, (pfc() - tic) * 1000
        )
    )

    tic = pfc()
    answer_2 = solution_2(input)
    print(
        "Answer to part 2 is: '{}'. Obtained in {:.2f} ms.".format(
            answer_2, (pfc() - tic) * 1000
        )
    )
