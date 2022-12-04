# my task solution
def include(arr, item):
    return item in arr


print(include([1, 2, 3, 4], 3))


# codewars task best solution
include = lambda a, i: i in a


# codewars task best solution
def include(arr, item):
    for i in arr:
        if i == item:
            return True
    return False