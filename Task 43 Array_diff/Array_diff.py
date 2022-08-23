# my task solution
def array_diff(a, b):
    return [i for i in a if i not in b]


print(array_diff([1, 2, 2], [2]))


# codewars task best solution
def array_diff(a, b):
    if len(b) == 0:
        return a

    for i in b:
        if i in a:
            for n in range(a.count(i)):
                a.remove(i)
    return a


# codewars task best solution
def array_diff(a, b):
    return [x for x in a if x not in set(b)]


# codewars task best solution
def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]