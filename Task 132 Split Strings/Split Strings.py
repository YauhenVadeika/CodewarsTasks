# my task solution
def solution(s):
    lst = [i for i in (s + '_' if len(s) % 2 != 0 else s)]
    return ["".join([lst[i], lst[i + 1]]) for i in range(0, len(lst), 2)]


print(solution('abc'))
print(solution('abcdef'))
print(solution('asdfadsf'))
print(solution(""))
print(solution("x"))


# codewars task best solution
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i + 2])
    return result


# codewars task best solution
import re

def solution(s):
    return re.findall(".{2}", s + "_")


# codewars task best solution
def solution(s):
    return [
        s[x:x + 2] if x < len(s) - 1 else s[-1] + "_"
        for x in range(0, len(s), 2)
    ]


# codewars task best solution
def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]
