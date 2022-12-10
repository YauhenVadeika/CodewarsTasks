# my task solution
def tower_builder(n_floors):
    return [(i * "*").center((n_floors * 2) - 1)
            for i in range((n_floors - n_floors) + 1, 2 * n_floors, 2)]


print(tower_builder(1))
print(tower_builder(3))
print(tower_builder(6))


# codewars task best solution
def tower_builder(n):
    return [("*" * (i * 2 - 1)).center(n * 2 - 1) for i in range(1, n + 1)]


# codewars task best solution
def tower_builder(n):
    return [
        " " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1)
        for i in range(n)
    ]


# codewars task best solution
def tower_builder(n_floors):
    if n_floors == 0:
        return []

    count = 1
    result = []

    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        result.append(space + stars + space)

    return result


# codewars task best solution
def tower_builder(n):
    length = n * 2 - 1
    return ['{:^{}}'.format('*' * a, length) for a in xrange(1, length + 1, 2)]


# codewars task best solution
tower_builder = lambda n: [
    str.center('*' * i, n * 2 - 1) for i in range(1, n * 2, 2)
]
