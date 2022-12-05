# my task solution
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError

    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(5))
print(factorial(-1))
print(factorial(13))
print(factorial(14))


# codewars task best solution
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n * factorial(n - 1)


# codewars task best solution
import math


def factorial(n):
    if 0 <= n <= 12:
        return math.factorial(n)
    else:
        raise ValueError("value out of range")


# codewars task best solution
def factorial(n):
    output = 1
    if n > 12 or n < 0:
        raise ValueError
    else:
        for x in range(1, n + 1):
            output *= x
        return output


# codewars task best solution
factorial = lambda n: __import__("math").factorial(n) if 0 <= n < 13 else int("x")
