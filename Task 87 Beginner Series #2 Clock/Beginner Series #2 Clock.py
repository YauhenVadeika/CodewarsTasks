# my task solution
def past(h, m, s):
    return 1000 * (60 * ((h * 60) + m) + s)


print(past(0, 1, 1))
print(past(1, 1, 1))
print(past(0, 0, 0))
print(past(1, 0, 1))
print(past(1, 0, 0))


# codewars task best solution
def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000


# codewars task best solution
def past(h, m, s):
    return 3600000 * h + 60000 * m + 1000 * s
