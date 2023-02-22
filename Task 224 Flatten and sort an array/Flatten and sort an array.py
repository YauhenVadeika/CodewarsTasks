# my task solution
def flatten_and_sort(array):

    return sorted([i for i in array if i for i in i])


print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]))
print(flatten_and_sort([[], []]))
print(flatten_and_sort([]))


# codewars task best solution
def flatten_and_sort(array):
    return sorted([j for i in array for j in i])


# codewars task best solution
from itertools import chain


def flatten_and_sort(array):
    return sorted((chain(*array)))


# codewars task best solution
def flatten_and_sort(array):
    return sorted(sum(array, []))


# codewars task best solution
def flatten_and_sort(array):
    newList = []
    for item in array:
        newList += item
    return sorted(newList)


# codewars task best solution
def flatten_and_sort(_a):
    return sorted([arr for x in _a for arr in x])
