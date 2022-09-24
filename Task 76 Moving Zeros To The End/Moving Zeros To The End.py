# my task solution
def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(0)
            lst.append(i)
    return lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))


# codewars task best solution
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l + [0] * (len(arr) - len(l))


# codewars task best solution
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


# codewars task best solution
def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)
