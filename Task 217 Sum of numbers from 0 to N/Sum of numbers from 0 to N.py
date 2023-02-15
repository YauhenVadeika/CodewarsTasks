# my task solution
def show_sequence(n):
    s = '0'
    for i in range(1, n + 1):
        s += '+' + str(i)
    return s + ' = ' + str(n * (n + 1) //
                           2) if n > 0 else '0=0' if n == 0 else str(n) + '<0'


print(show_sequence(6))
print(show_sequence(0))
print(show_sequence(-1))


# codewars task best solution
def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    else:
        counter = sum(range(n + 1))
        return '+'.join(map(str, range(n + 1))) + " = " + str(counter)


# codewars task best solution
def show_sequence(n):
    if n == 0:
        return "0=0"
    return "{} = {}".format("+".join(map(str, range(n + 1))), sum(
        range(n + 1))) if n > 0 else "{}<0".format(n)


# codewars task best solution
def show_sequence(n):
    if n < 0:
        return str(n) + '<0'
    if n == 0:
        return '0=0'
    s = list(range(n + 1))
    return '+'.join([str(i) for i in s]) + ' = ' + str(sum(s))


# codewars task best solution
def show_sequence(n):
    s = 0
    full_s = []
    res = ""
    if n > 0:
        for i in range(n + 1):
            s += i
            full_s.append(str(i))
        res = str('+'.join(full_s)) + " = " + str(s)
    elif n == 0:
        res = "0=0"
    else:
        res = str(n) + "<0"
    return res


# codewars task best solution
def show_sequence(n):
    return f'{"+".join(str(i) for i in range(n+1))} = {int(n*(n+1)/2)}'.replace(
        '0 = 0', '0=0') if n >= 0 else f'{n}<0'
