# my task solution
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return factorial(n - 1) * n


print(factorial(0))
print(factorial(1))
print(factorial(3))


# codewars task best solution
def factorial(n):
    j = 1
    for i in range(1, n + 1):
        j *= i
    return j


# codewars task best solution
from functools import reduce
from operator import imul


def factorial(n):
    return reduce(imul, range(1, n + 1), 1)


# codewars task best solution
from math import factorial as fac


def factorial(n):
    return fac(n)


# codewars task best solution
def factorial(n):
    if n < 0:
        raise ValueError("negative value cannot be calculated")

    elif n == 0:
        return 1

    else:
        z = 1
        for i in range(2, n + 1):
            z *= i
        return z


# codewars task best solution
def factorial(n):
    if n < 2: return 1
    else: return n * factorial(n - 1)
