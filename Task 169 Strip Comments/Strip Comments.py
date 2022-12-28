# my task solution
def solution(strng, markers):
    parts = strng.split('\n')
    for i in markers:
        parts = [v.split(i)[0].rstrip() for v in parts]
    return '\n'.join(parts)


print(
    solution('apples, pears # and bananas\ngrapes\nbananas !apples',
             ['#', '!']))


# codewars task best solution
def strip_line(line, markers):
    for m in markers:
        if m in line:
            line = line[:line.index(m)]
    return line.rstrip()


def solution(string, markers):
    stripped = [strip_line(l, markers) for l in string.splitlines()]
    return '\n'.join(stripped)


# codewars task best solution
def solution(string, markers):
    s = string.splitlines()
    for i in range(len(s)):
        for j in markers:
            if j in s[i]:
                s[i] = s[i][:s[i].index(j)].rstrip()
    return "\n".join(s)


# codewars task best solution
solution = lambda t, m, r=__import__('re'): r.sub(
    r'( *[{}].*)'.format(r.escape(''.join(m))), '', t) if m else t

# codewars task best solution
import re


def solution(string, markers):
    return string if not markers else re.sub(
        f" *[{re.escape(''.join(markers))}].*", "", string, re.MULTILINE)
