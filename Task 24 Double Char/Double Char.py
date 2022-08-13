# my task solution
def double_char(s):
    return "".join([i * 2 for i in s])


print(double_char("String"))


# codewars task best solution
def double_char(s):
    return ''.join(c * 2 for c in s)


# codewars task best solution
def double_char(s):
    res = ''
    for i in s:
        res += i * 2
    return res
