"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def persistence(n):

    if n < 10:
        return 0
    else:
        i = 1
        for j in range(len(str(n))):
            i = i * int(str(n)[j])
        return persistence(i) + 1


print(persistence(999))  # --> 4
print(persistence(4))
print(persistence(39))

# codewars task best solution
import operator


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i


# codewars task best solution
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
    # your code


# codewars task best solution
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist


# codewars task best solution
from operator import mul


def persistence(n):
    return 0 if n < 10 else persistence(
        reduce(mul, [int(i) for i in str(n)], 1)) + 1


# codewars task best solution
def persistence(n):
    if n < 10: return 0
    mult = 1
    while (n > 0):
        mult = n % 10 * mult
        n = n // 10
    return persistence(mult) + 1


# codewars task best solution
def multiply_digits(n):
    product = 1
    while (n > 0):
        product *= n % 10
        n //= 10

    return product


def persistence(n):
    count = 0
    while (n > 9):
        n = multiply_digits(n)
        count += 1

    return count


# codewars task best solution
persistence = lambda n, c=0: persistence(
    reduce(lambda x, y: int(x) * int(y), str(n)), c + 1) if n >= 10 else c
