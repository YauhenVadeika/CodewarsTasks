# my task solution
def find_outlier(integers):
    b = []
    c = []
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            b.append(integers[i])
        if integers[i] % 2 != 0:
            c.append(integers[i])
    return c[0] if len(b) > len(c) else b[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([1, 2, 3]))


# dewars task best solution
def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


# dewars task best solution
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]
