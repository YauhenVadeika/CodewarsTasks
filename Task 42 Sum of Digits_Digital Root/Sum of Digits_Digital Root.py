# my task solution
def digital_root(n):
    while True:
        res = sum([int(i) for i in str(n)])

        if len(str(res)) > 1:
            n = res
        else:
            return res


print(digital_root(942))
print(digital_root(493193))


# codewars task best solution
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# codewars task best solution
def digital_root(n):
    return n % 9 or n and 9


# codewars task best solution
def digital_root(n):
    # ...
    while n > 9:
        n = sum(map(int, str(n)))
    return n