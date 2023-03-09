# my task solution
def no_boring_zeros(n):
    return 0 if n == 0 else int(str(n).rstrip("0"))


print(no_boring_zeros(1450))
print(no_boring_zeros(-1050))
print(no_boring_zeros(960000))
print(no_boring_zeros(0))


# codewars task best solution
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0


# codewars task best solution
def no_boring_zeros(n):
    if n == 0:
        return n
    while n % 10 == 0:
        n = n / 10
    return n


# codewars task best solution
def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n


# codewars task best solution
def no_boring_zeros(n):
    return int(str(n).strip('0') or 0)


# codewars task best solution
def no_boring_zeros(n):
    while n and n % 10 == 0:
        n /= 10
    return n