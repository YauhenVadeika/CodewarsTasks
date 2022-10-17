# my task solution
def grow(arr):
    var = 1
    for i in arr:
        var *= i
    return var


print(grow([1, 2, 3, 4]))

# codewars task best solution
from functools import reduce


def grow(arr):
    return reduce(lambda x, y: x * y, arr)


# codewars task best solution
import math


def grow(arr):
    return math.prod(arr)


# codewars task best solution
def grow(arr):
    return eval('*'.join([str(i) for i in arr]))