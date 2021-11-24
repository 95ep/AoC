import re

def load_input(path):
    inpt = []
    with open(path) as f:
        for line in f:
            inpt.append(line)

    start = int(inpt[0])
    r = r"(\d+)"
    busses = [int(x) for x in re.findall(r, inpt[1])]

    return start, busses


def task1(start, busses):
    wait_time = [ (start // id + 1) * id - start for id in busses]
    print(wait_time)
    min_wait, idx = min((val, idx) for (idx, val) in enumerate(wait_time))
    print(min_wait)
    print(idx)
    return min_wait * busses[idx]

start, busses = load_input('inputs/day13.txt')

print(f"{task1(start, busses)}")