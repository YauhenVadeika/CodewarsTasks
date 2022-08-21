# my task solution
def expanded_form(num):
    lst = []
    item = len(str(num)) - 1
    for n in str(num):
        if n != "0":
            lst.append(n + "0" * item)
        item -= 1
    return " + ".join(lst)


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))


# codewars task best solution
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y, x in enumerate(num) if x != '0')


# codewars task best solution
def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
