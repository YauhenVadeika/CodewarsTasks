# my task solution
import math


def round_to_next5(n):
    return math.ceil(n / 5) * 5


print(round_to_next5(0))
print(round_to_next5(1))
print(round_to_next5(12))
print(round_to_next5(25))
print(round_to_next5(30))
print(round_to_next5(-2))
print(round_to_next5(-5))
print(round_to_next5(-7))


# codewars task best solution
def round_to_next5(n):
    return n + (5 - n) % 5


# codewars task best solution
def round_to_next5(n):
    while n % 5 != 0:
        n += 1
    return n


# codewars task best solution
def round_to_next5(n):
    # Your code here
    return n + -n % 5


# codewars task best solution
def round_to_next5(n):
    # Your code here
    rem = n % 5
    return n + ((5 - rem) if rem else 0)


# codewars task best solution
def round_to_next5(n):
    return n if n % 5 == 0 else round_to_next5(n + 1)


# codewars task best solution
def round_to_next5(n):
    return (n + 4) // 5 * 5
