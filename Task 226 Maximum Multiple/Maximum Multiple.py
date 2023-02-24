# my task solution
def max_multiple(divisor, bound):
    return bound - (bound % divisor)


print(max_multiple(2, 7))
print(max_multiple(3, 10))
print(max_multiple(7, 17))


# codewars task best solution
def max_multiple(divisor, bound):
    return bound // divisor * divisor


# codewars task best solution
def max_multiple(divisor, bound):
    l = []
    for int in range(bound + 1):
        if int % divisor == 0:
            l.append(int)
    return max(l)


# codewars task best solution
max_multiple = lambda divisor, bound: bound - (bound % divisor)


# codewars task best solution
def max_multiple(divisor, bound):
    m = bound // divisor
    return divisor * m


# codewars task best solution
def max_multiple(divisor, bound):
    return max([n for n in range(bound + 1) if n % divisor == 0])

#your code here
