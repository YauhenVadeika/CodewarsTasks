# my task solution
def reverse_list(l):
    l.reverse()
    return l


print(reverse_list([1, 2, 3, 4]))
print(reverse_list([3, 1, 5, 4]))
print(reverse_list([3, 6, 9, 2]))
print(reverse_list([1]))


# codewars task best solution
def reverse_list(l):
    return l[::-1]


# codewars task best solution
def reverse_list(l):
    """return a list with the reverse order of l"""
    return list(reversed(l))


# codewars task best solution
reverse_list = lambda l: l[::-1]


# codewars task best solution
def reverse_list(l):
    new_list = []
    for i in l:
        new_list = [i] + new_list
    return new_list


# codewars task best solution
def reverse_list(l):
    return [r for r in reversed(l)]


# codewars task best solution
reverse_list = lambda _: _[::-1]