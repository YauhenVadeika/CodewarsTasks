# my task solution
def maps(a):
    return [i * 2 for i in a]


# print(maps([1, 2, 3]))
# print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(maps([]))


# codewars task best solution
def maps(a):
    return [2 * x for x in a]


# codewars task best solution
def maps(a):
    return map(lambda x: 2 * x, a)
