# my task solution
def snail(snail_map):

    a = []

    while snail_map:
        a.extend(list(snail_map.pop(0)))
        snail_map = list(zip(*snail_map))
        snail_map.reverse()
    return a


print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# codewars task best solution
import numpy as np


def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


# codewars task best solution
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret


# codewars task best solution
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1]  # Rotate
    return out