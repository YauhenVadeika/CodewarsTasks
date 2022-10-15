# my task solution
def number(lines):
    return [f'{i+1}: {lines[i]}' for i in range(len(lines))]


print(number(["a", "b", "c"]))


# codewars task best solution
def number(lines):
    return ['%d: %s' % v for v in enumerate(lines, 1)]


# codewars task best solution
def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]


# codewars task best solution
def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]


# codewars task best solution
def number(lines):
    
    a = []
    
    for i, c in enumerate(lines, 1):
        str_var = str(i) + ': ' + str(c)
        a.append(str_var)
    return a

