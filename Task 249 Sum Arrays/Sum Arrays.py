# my task solution
def sum_array(a):
    return sum(a)


print(sum_array([1, 2, 3]))
print(sum_array([1.1, 2.2, 3.3]))
print(sum_array(range(101)))
print(sum_array([]))


# codewars task best solution
def sum_array(a):
    return sum(a) if a else 0


# codewars task best solution
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum


# codewars task best solution
from typing import List


def sum_array(a: List[int]) -> int:
    """ Get the sum of elements given in the array. """
    return sum(a)


# codewars task best solution
def sum_array(a):
    total = 0
    i = 0
    while i < len(a):
        total += a[i]
        i += 1
    return total


# codewars task best solution
sum_array = lambda a: sum(a)