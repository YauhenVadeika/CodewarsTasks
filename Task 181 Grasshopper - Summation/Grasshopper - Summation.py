# my task solution
def summation(num):
    """recursion
    """
    step = 0
    if step == num:
        return num
    else:
        return summation(num - 1) + num


print(summation(8))
print(summation(213))
print(summation(100))


# # # my task solution
def summation(num):
    """range
    """
    return sum(range(num + 1))


print(summation(8))
print(summation(213))
print(summation(100))


# # my task solution
def summation(num):
    """ while
    """
    i = 0
    s = 0
    while num:
        s += 1
        i += s
        if s == num:
            return i


print(summation(8))
print(summation(213))
print(summation(100))


# my task solution
def summation(num):
    """List comprehension
    """
    return sum([i for i in range(num + 1)])


print(summation(8))
print(summation(213))
print(summation(100))


# codewars task best solution
def summation(num):
    return sum(xrange(num + 1))


# codewars task best solution
def summation(num):
    return (1 + num) * num / 2


# codewars task best solution
def summation(num):
    return sum(range(1, num + 1))


# codewars task best solution
def summation(num):
    return sum(range(num + 1))


# codewars task best solution
def summation(num):
    total = 0
    for i in range(0, num + 1):
        total = total + i
    return total


# codewars task best solution
summation = lambda n: n * -~n >> 1
