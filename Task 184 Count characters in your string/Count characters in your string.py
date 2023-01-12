# my task solution
def count(string):
    return {i: string.count(i) for i in string}


print(count('aba'))
print(count(''))

# codewars task best solution
from collections import Counter


def count(string):
    return Counter(string)


# codewars task best solution
def count(string):
    r = {}
    for c in string:
        if c in r:
            r[c] += 1
        else:
            r[c] = 1
    return r


# codewars task best solution
def count(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter


# codewars task best solution
def count(string):
    letters = {}
    for c in string:
        letters[c] = string.count(c)
    return letters


# codewars task best solution
def count(string):
    m, n = [], []
    for i in string:
        if i not in m:
            m.append(i)
            n.append(string.count(i))
    return dict(zip(m, n))


# codewars task best solution
def count(string):
    if string == "":
        return {}
    else:
        dict = {}
        for i in string:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        return dict