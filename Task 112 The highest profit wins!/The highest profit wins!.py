# my task solution
def min_max(lst):
    return [i for i in (min(lst), max(lst))]


print(min_max([1, 2, 3, 4, 5]))
print(min_max([2334454, 5]))
print(min_max([1]))


# codewars task best solution
def min_max(lst):
    return [min(lst), max(lst)]


# codewars task best solution
def min_max(lst):
    # Too easy, but requires two pases
    # return[min(lst), max(lst)]

    # Single pass:
    l, u = None, None
    for n in lst:
        if l is None or n < l:
            l = n
        if u is None or n > u:
            u = n
    return [l, u]


# codewars task best solution


def min_max(lst):
    lst.sort()
    tempor = [lst[0], lst[-1]]
    return tempor


# codewars task best solution
min_max = lambda l: [min(l), max(l)]