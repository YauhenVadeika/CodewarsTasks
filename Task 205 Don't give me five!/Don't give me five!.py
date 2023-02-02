# my task solution
def dont_give_me_five(start, end):

    return len([i for i in range(start, end + 1) if '5' not in str(i)])


print(dont_give_me_five(1, 9))
print(dont_give_me_five(4, 17))


# codewars task best solution
def dont_give_me_five(start, end):
    return sum('5' not in str(i) for i in range(start, end + 1))


# codewars task best solution
def dont_give_me_five(start, end):
    tick = 0
    for x in range(start, end + 1):
        if '5' not in str(x):
            tick += 1
    return tick


# codewars task best solution
def dont_give_me_five(start, end):
    n = []
    i = start
    while i <= end:
        m = str(i)
        if "5" in m:
            i += 1
        if "5" not in m:
            n.append(m)
            i += 1
    x = len(n)
    return x


# codewars task best solution
def dont_give_me_five(start, end):
    return sum([all_but_fives(i) for i in range(start, end + 1)])


def all_but_fives(i):
    """ Mathematical alternative to the common solution for this Kata. Slightly more efficient. """
    position = abs(i)
    while position != 0:
        figure = position % 10
        if figure == 5:
            return False
        position = position // 10
    return True


# codewars task best solution
def dont_give_me_five(start, end):
    print(start, end)
    res = [
        x for x in range(start, end + 1) if not (x % 5 == 0 and x % 2 == 1)
        and not (x // 10 % 5 == 0 and x // 10 % 2 == 1)
    ]
    print(res)
    return len(res)


# codewars task best solution
dont_give_me_five = lambda start, end: sum('5' not in str(a)
                                           for a in range(start, end + 1))
