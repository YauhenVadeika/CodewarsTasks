# my task solution
def add_binary(a, b):
    return bin(sum([a, b]))[2:]


print(add_binary(1, 1))
print(add_binary(5, 9))
print(add_binary(51, 12))
print(add_binary(0, 1))


# codewars task best solution
def add_binary(a, b):
    return bin(a + b)[2:]


# codewars task best solution
def add_binary(a, b):
    return '{0:b}'.format(a + b)


# codewars task best solution
def add_binary(a, b):
    n = a + b
    binList = []
    while (n > 0):
        binList.append(n % 2)
        n = n // 2
    return ''.join(map(str, reversed(binList)))


# codewars task best solution
add_binary = lambda a, b: bin(a + b)[2:]
