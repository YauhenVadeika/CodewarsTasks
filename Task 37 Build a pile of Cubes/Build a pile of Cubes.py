# my task solution
def find_nb(m):
    vs = 0
    s = 0
    while vs < m:
        s += 1
        vs += s**3
    return s if vs == m else -1


print(find_nb(1071225))
print(find_nb(91716553919377))


# codewars task best solution
def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1


# codewars task best solution
from math import floor, sqrt


def find_nb(m):
    # Used the formula for the sum of cubes: m = (n(n+1)/2)^2
    # Rearranged to find n^2 + n = n(n+1) ~= n^2 ~= 2sqrt(m),
    # so take square root and round down the result.
    n_canidate = int(floor(sqrt(2 * sqrt(m))))
    if (n_canidate * (n_canidate + 1) / 2)**2 == m:
        return n_canidate
    else:
        return -1