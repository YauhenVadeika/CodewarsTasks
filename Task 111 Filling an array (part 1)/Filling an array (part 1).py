# my task solution
def arr(n=0):
    return list(range(n))


print(arr(5))
print(arr(0))
print(arr())


# codewars task best solution
def arr(n=0):
    return [i for i in range(n)]


# codewars task best solution
def arr(n=0):
    return [*range(n)]


# codewars task best solution
def arr(n=0):
    # [ the numbers 0 to N-1 ]
    aux = []
    for x in range(n):
        aux.append(x)
    return aux


# codewars task best solution
arr = lambda n=0: list(range(n))