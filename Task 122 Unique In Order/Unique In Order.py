# my task solution
def unique_in_order(iterable):
    return [
        iterable[i] for i in range(len(iterable))
        if i == 0 or iterable[i] != iterable[i - 1]
    ]


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))


# codewars task best solution
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


# codewars task best solution
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


# codewars task best solution
unique_in_order = lambda l: [
    z for i, z in enumerate(l) if i == 0 or l[i - 1] != z
]
