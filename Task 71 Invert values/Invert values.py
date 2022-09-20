# my task solution
def invert(lst):
    return [i * (-1) if i > 0 else i * (-1) for i in lst]


print(invert([1, -2, 3, -4, 5]))
print(invert([1, 2, 3, 4, 5]))
print(invert([-1, -2, -3, -4, -5]))
print(invert([-1, -2, -3, -4, 5]))
print(invert([]))


# codewars task best solution
def invert(lst):
    return [-x for x in lst]


# codewars task best solution
def invert(lst):
    return list(map(lambda x: -x, lst))


# codewars task best solution
def invert(lst):
    i = 0
    inv = []
    while i < len(lst):
        inv.append(lst[i] * -1)
        i += 1
    return inv