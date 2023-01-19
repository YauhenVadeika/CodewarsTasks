# my task solution
import math


def find_divisors(num):
    divisors = set()
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            divisors.add(i)
            divisors.add(int(num / i))
    total = sum(list(map(lambda x: x**2, list(divisors))))
    if (int(math.sqrt(total))**2 == total) and total > 0:
        return [num, total]
    return False


def list_squared(m, n):
    output = []
    for num in range(m, n + 1):
        soltn = find_divisors(num)
        if soltn:
            output.append(soltn)
    return output


print(list_squared(1, 250))

# codewars task best solution
CACHE = {}


def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number]

    return CACHE[number]


def list_squared(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum**0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret


# codewars task best solution
def list_squared(m, n):
    out = []
    for i in range(m, n + 1):
        # Finding all divisors below the square root of i
        possibles = set([x for x in range(1, int(i**0.5) + 1) if i % x == 0])
        # And adding their counterpart
        possibles.update([i / x for x in possibles])
        # Doubles in the possibles are solved due to the set
        val = sum(x**2 for x in possibles)
        # Checking for exact square
        if (int(val**0.5))**2 == val: out.append([i, val])
    return out


# codewars task best solution
from math import floor, sqrt, pow


def sum_squared_factors(n):
    s, res, i = 0, [], 1
    while (i <= floor(sqrt(n))):
        if (n % i == 0):
            s += i * i
            nf = n // i
            if (nf != i):
                s += nf * nf
        i += 1
    if (pow(int(sqrt(s)), 2) == s):
        res.append(n)
        res.append(s)
        return res
    else:
        return None


def list_squared(m, n):
    res, i = [], m
    while (i <= n):
        r = sum_squared_factors(i)
        if (r != None):
            res.append(r)
        i += 1
    return res


# codewars task best solution


def get_divisors_sum(n):
    """Get the divisors: iterate up to sqrt(n), check if the integer divides n with r == 0
        Return the sum of the divisors squared."""
    divs = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.extend([i, int(n / i)])
    divs.extend([n])

    # Get sum, return the sum
    sm = sum([d**2 for d in list(set(divs))])
    return sm


def list_squared(m, n):
    """Search for squares amongst the sum of squares of divisors of numbers from m to n """
    out = []
    for j in range(m, n + 1):
        s = get_divisors_sum(j)  # sum of divisors squared.
        if (s**0.5).is_integer():  # check if a square.
            out.append([j, s])
    return out


# codewars task best solution
def list_squared(m, n):
    g = lambda x: sum([i**2 for i in range(2, (x + 1) // 2 + 1)
                       if not x % i] + [1, x**2])
    s = [] if m != 1 else [[1, 1]]
    for i in range(m, n + 1):
        k = g(i)
        q = k**0.5
        if int(q) == q:
            s.append([i, k])
    return s