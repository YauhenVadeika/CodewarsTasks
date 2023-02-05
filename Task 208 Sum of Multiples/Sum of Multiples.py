# my task solution
def sum_mul(n, m):
    array = []
    if m <= 0 or n <= 0:
        return "INVALID"
    if m <= 0 and n <= 0:
        return "INVALID"
    for i in range(n, m):
        if i % n == 0:
            array.append(i)
    return sum(array)


print(sum_mul(2, 9))
print(sum_mul(3, 13))
print(sum_mul(4, -123))


# codewars task best solution
def sum_mul(n, m):
    if m > 0 and n > 0:
        return sum(range(n, m, n))
    else:
        return 'INVALID'


# codewars task best solution
def sum_mul(n, m):
    return sum(x for x in range(n, m, n)) if m > 0 and n > 0 else 'INVALID'


# codewars task best solution
def sum_mul(n, m):
    return sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"


# codewars task best solution
def sum_mul(n, m):
    sumu = 0
    if n > 0 and m > 0:
        for i in range(n, m):
            if (i % n == 0):
                sumu += i
    else:
        return 'INVALID'
    return sumu


# codewars task best solution
sum_mul = lambda n, m: sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"


# codewars task best solution
def sum_range(end, divisor=None):
    if divisor:
        return int(sum_range(end // divisor)) * divisor
    return end * (end + 1) / 2


def sum_mul(n, m):
    return sum_range(m - 1, divisor=n) if n > 0 and m > 0 else 'INVALID'
