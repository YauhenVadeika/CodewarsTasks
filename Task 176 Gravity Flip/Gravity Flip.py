# my task solution
def flip(d, a):
    return sorted(a) if d == "R" else sorted(a)[::-1]


print(flip('R', [3, 2, 1, 2]))
print(flip('L', [1, 4, 5, 3, 5]))


# codewars task best solution
def flip(d, a):
    return sorted(a, reverse=d == 'L')


# codewars task best solution
def flip(d, a):
    if d == 'L':
        return sorted(a, reverse=True)
    else:
        return sorted(a)


# codewars task best solution
def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a, reverse=True)


# codewars task best solution
def flip(d, a):
    if d == 'R':
        a.sort()
        return a
    else:
        a.sort()
        a = a[::-1]
        return a


# codewars task best solution
flip = lambda d, a: sorted(a, reverse=d == 'L')
