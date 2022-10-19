# my task solution
def find_next_square(sq):
    return int(((sq**0.5) + 1)**2) if (sq**0.5) == int(sq**0.5) else -1


print(find_next_square(121))
print(find_next_square(114))
print(find_next_square(625))


# codewars task best solution
def find_next_square(sq):
    root = sq**0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


# codewars task best solution
def find_next_square(sq):
    x = sq**0.5
    return -1 if x % 1 else (x + 1)**2


# codewars task best solution
import math


def find_next_square(sq):
    return (math.sqrt(sq) + 1)**2 if (math.sqrt(sq)).is_integer() else -1


# codewars task best solution
from math import sqrt


def find_next_square(sq):
    return (sqrt(sq) + 1)**2 if sqrt(sq) % 1 == 0 else -1
