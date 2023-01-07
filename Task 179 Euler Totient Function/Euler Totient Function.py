# my task solution
def totient(n):
    if (n is None) or (n == str(n)) or (n < 0):
        return 0
    if n == 1:
        return 1
    else:
        f = int(n > 1 and n)
        for p in range(2, int(n**.5) + 1):
            if not n % p:
                f -= f // p
                while not n % p:
                    n //= p

        if n > 1:
            f -= f // n
        return f


print(totient(1))
print(totient(0))
print(totient(7))
print(totient("a"))
print(totient(-1))
print(totient(None))


# codewars task best solution
def totient(n):
    try:
        assert isinstance(n, int) and n > 0
        phi = n
        if not n % 2:
            phi -= phi // 2
            while not n % 2:
                n //= 2
        for p in range(3, int(n**.5) + 1, 2):
            if not n % p:
                phi -= phi // p
                while not n % p:
                    n //= p
        if n > 1: phi -= phi // n
        return phi
    except:
        return 0


# codewars task best solution
def totient(n):
    if not isinstance(n, int) or n < 1: return 0

    phi = n >= 1 and n
    for p in range(2, int(n**.5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    if n > 1: phi -= phi // n
    return phi


# codewars task best solution
from itertools import count, chain
from fractions import Fraction
from functools import reduce
from operator import mul


def primes(n):
    for x in chain([2], count(3, 2)):
        if n == 1: return
        if x**2 > n:
            yield Fraction(n - 1, n)
            return
        elif not n % x:
            yield Fraction(x - 1, x)
            while not n % x:
                n //= x


def totient(n):
    return reduce(mul, primes(n), n) if type(n) == int and n >= 1 else 0


# codewars task best solution
def totient(n):
    if not isinstance(n, int) or n < 1:
        return 0
    if n == 1:
        return 1
    pf = prime_factors(n)
    nums, dens = 1, 1
    for p in pf:
        dens *= p
        nums *= p - 1
    return n * nums // dens


def prime_factors(n):
    f = 2
    prime_facs = []
    while (f * f <= n):
        if n % f == 0:
            n //= f
            prime_facs.append(f)
        else:
            f += 1
    prime_facs.append(n)
    return set(prime_facs)
