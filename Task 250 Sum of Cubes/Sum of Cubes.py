# my task solution
def sum_cubes(n):
    return sum([i**3 for i in range(1, n + 1)])


print(sum_cubes(2))
print(sum_cubes(1))
print(sum_cubes(10))
print(sum_cubes(123))


# codewars task best solution
def sum_cubes(n):
    return sum(i**3 for i in range(0, n + 1))


# codewars task best solution
def sum_cubes(n):
    return sum(x**3 for x in range(n + 1))


# codewars task best solution
def sum_cubes(n):
    return (n * (n + 1) // 2)**2


# codewars task best solution
def sum_cubes(n):
    result = 0
    for i in range(n + 1):
        result = result + i**3

    return result


# codewars task best solution
def sum_cubes(n):
    return sum(map(lambda x: x**3, range(1, n + 1)))
