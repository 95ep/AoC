import re

def evaluate_exp(exp):
    while exp.rfind('(') != -1:
        i1 = exp.rfind('(')
        i2 = exp.find(')', i1)
        val = evaluate_exp(exp[i1+1: i2])
        if i2 < (len(exp) - 1):
            exp = exp[:i1] + str(val) + exp[i2+1:]
        else:
            exp = exp[:i1] + str(val)

    match = re.match(r"(\d+) ([+*]) (\d+)", exp)
    while match:
        g = match.groups()
        if g[1] == '+':
            val = int(g[0]) + int(g[2])
        else:
            val = int(g[0]) * int(g[2])

        exp = str(val) + ' ' + exp[match.span()[1]+1:]
        match = re.match(r"(\d+) ([+*]) (\d+)", exp)

    return val

sum = 0
with open('inputs/day18.txt') as f:
    for line in f:
        sum += evaluate_exp(line)

print(sum)