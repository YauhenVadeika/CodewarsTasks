# my task solution
def dig_pow(n, p):
    num = str(n)
    total = sum([int(num[i])**(p + i) for i in range(len(num))])
    return total / n if (total % n) == 0 else -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))


# codewars task best solution
def dig_pow(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s / n if s % n == 0 else -1


# codewars task best solution
def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k
