# my task solution
def between(a, b):
    return list(range(a, b + 1))


print(between(1, 4))
print(between(-2, 2))


# codewars task best solution
def between(a, b):
    return [result for result in range(a, b + 1)]


# codewars task best solution
def between(a, b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr
