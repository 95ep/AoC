import re


def parse_input(path):
    input = []
    sub_list = []
    with open(path) as f:
        for line in f:
            if re.match(r"\$", line):
                if sub_list:
                    input.append(sub_list)
                sub_list = [line.rstrip()]

            else:
                if line.rstrip():
                    sub_list.append(line.rstrip())

    input.append(sub_list)
    return input


def calc_dir_size(inp):
    size_dict = {}
    pwd = []
    for cmd in inp:
        match = re.match("\$ cd (.+)", cmd[0])
        if match:
            if match.group(1) == "..":
                pwd.pop()
            else:
                pwd.append(match.group(1))
        elif cmd[0] == "$ ls":
            for line in cmd:
                file_match = re.match("(\d+) \D+", line)
                if file_match:
                    file_size = int(file_match.group(1))
                    path = ""
                    for element in pwd:
                        path += element
                        if path in size_dict:
                            size_dict[path] += file_size
                        else:
                            size_dict[path] = file_size
    return size_dict


def summarize_small_dirs(size_dict):
    tot_size = 0
    for size in size_dict.values():
        if size < 100001:
            tot_size += size

    return tot_size


def find_delete_folder(size_dict, limit):
    candidates = []
    for size in size_dict.values():
        if size >= limit:
            candidates.append(size)
    candidates.sort()
    return candidates[0]


def solution_1(input_path):
    inp = parse_input(input_path)
    dir_sizes = calc_dir_size(inp)
    return summarize_small_dirs(dir_sizes)


def solution_2(input_path):
    inp = parse_input(input_path)
    dir_sizes = calc_dir_size(inp)
    space_missing = 30000000 - (70000000 - dir_sizes["/"])
    return find_delete_folder(dir_sizes, space_missing)


if __name__ == "__main__":
    input_path = "y2022/inputs/day07.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
