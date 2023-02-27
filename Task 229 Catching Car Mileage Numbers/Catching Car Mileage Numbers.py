# my task solution
def num_interesting(number):

    if number % 100 == number:
        print("It's not a big number")
        return False

    if number % 100 == 0:
        print("Followed by zeroes")
        return True

    number = str(number)

    if len(set(number)) == 1:
        print("Has same digits")
        return True

    if number[::-1] == number:
        print("Palindrome")
        return True

    if number in '1234567890':
        print("Sequential increasing")
        return True

    if number in '9876543210':
        print("Sequential decreasing")
        return True


def is_interesting(number, awesome_phrases):

    if number + 1 in awesome_phrases or number + 2 in awesome_phrases:
        return 1

    if number in awesome_phrases:
        return 2

    if num_interesting(number):
        return 2

    if num_interesting(number + 1) or num_interesting(number + 2):
        return 1

    return 0


# codewars task best solution
def is_incrementing(number):
    return str(number) in '1234567890'


def is_decrementing(number):
    return str(number) in '9876543210'


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def is_round(number):
    return set(str(number)[1:]) == set('0')


def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing, is_palindrome,
             awesome_phrases.__contains__)

    for num, color in zip(range(number, number + 3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0


# codewars task best solution
def is_good(n, awesome):
    return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(
        n)[::-1] or int(str(n)[1:]) == 0


def is_interesting(n, awesome):
    if n > 99 and is_good(n, awesome):
        return 2
    if n > 97 and (is_good(n + 1, awesome) or is_good(n + 2, awesome)):
        return 1
    return 0


# codewars task best solution
import re


def is_sequential(string):
    return string in "1234567890" or string in "9876543210"


def is_interesting(number, awesome_phrases):
    print(number)
    interestingness = 2
    for i in (number, number + 1, number + 2):
        if (number != i):
            interestingness = 1
        if (i < 100):
            continue
        if (i in awesome_phrases):
            return interestingness
        i = str(i)
        if re.match(r"^\d0+$", i):
            return interestingness
        if i == i[::-1]:
            return interestingness
        if is_sequential(i):
            return interestingness
        if re.match(r"^(\d)\1+$", i):
            return interestingness

    return 0


# codewars task best solution
def is_interesting(n, awesome_phrases):
    import math
    for m in range(3):
        s = str(n + m)
        if len(s) > 2 and (zf(s) or sd(s) or seqinc(s) or seqdec(s) or pal(s)
                           or awe(s, awesome_phrases)):
            if m == 0: return 2
            else: return 1
    return 0


def awe(s, l):
    return s in [str(x) for x in l]


def pal(s):
    return s == s[::-1]


def seqdec(s):
    a = '9876543210'
    for i in range(len(s) - 1):
        if a.index(s[i]) + 1 != a.index(s[i + 1]): return False
    return True


def seqinc(s):
    a = '1234567890'
    for i in range(len(s) - 1):
        if a.index(s[i]) + 1 != a.index(s[i + 1]): return False
    return True


def sd(s):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]: return False
    return True


def zf(s):
    for i in range(1, len(s)):
        if s[i] != '0': return False
    return True


# codewars task best solution
def is_interesting(number, awesome_phrases):

    def check(n):
        nonlocal awesome_phrases
        n = str(n)
        test0 = lambda x: len(x) > 2
        test1 = lambda x: set(x[1:]) == set("0")
        test2 = lambda x: len(set(x)) == 1
        test3 = lambda x: all(
            (int(b) or 10) - (int(a) or 10) == 1 for a, b in zip(x, x[1:]))
        test4 = lambda x: all(int(a) - int(b) == 1 for a, b in zip(x, x[1:]))
        test5 = lambda x: x == x[::-1]
        test6 = lambda x: int(x) in awesome_phrases
        return test0(n) and (test1(n) or test2(n) or test3(n) or test4(n)
                             or test5(n) or test6(n))

    return int((check(number) and 2)
               or (check(number + 1) or check(number + 2)))
