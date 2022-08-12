# my task solution
def printer_error(s):
    num = 0
    for i in range(0, len(s)):
        if s[i] not in "abcdefghijklm":
            num += 1
    return f'{str(num)}/{len(s)}'


# codewars task best solution
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]", '', s)), len(s))


# codewars task best solution
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
