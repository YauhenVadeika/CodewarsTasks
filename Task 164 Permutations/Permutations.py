# my task solution
def permutations(s):
    res = set([s])
    if len(s) == 2:
        res.add(s[1] + s[0])

    elif len(s) > 2:
        for i, x in enumerate(s):
            for j in permutations(s[:i] + s[i + 1:]):
                res.add(x + j)

    return list(res)


print(permutations("a"))
print(permutations("ab"))
print(permutations("aabb"))

# codewars task best solution
import itertools


def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


# codewars task best solution
def permutations(string):
    if len(string) == 1: return set(string)
    first = string[0]
    rest = permutations(string[1:])
    result = set()
    for i in range(0, len(string)):
        for p in rest:
            result.add(p[0:i] + first + p[i:])
    return result


# codewars task best solution
def permutations(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        return set(s[i] + p for i in range(len(s))
                   for p in permutations(s[:i] + s[i + 1:]))


# codewars task best solution
def permutations(s):
    if (len(s) == 1): return [s]
    result = []
    for i, v in enumerate(s):
        result += [v + p for p in permutations(s[:i] + s[i + 1:])]
    return list(set(result))


# codewars task best solution
def permutations(word):
    if len(word) <= 1:
        return [word]

    perms = permutations(word[1:])
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + char + perm[i:])
    return set(result)