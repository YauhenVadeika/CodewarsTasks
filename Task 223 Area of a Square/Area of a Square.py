# my task solution
import math


def square_area(A):

    return round((2 * A / (math.pi))**2, 2)


print(square_area(2))
print(square_area(14.05))

# codewars task best solution
from math import pi


def square_area(A):
    return round((2 * A / pi)**2, 2)


# codewars task best solution
import math


def square_area(A):
    return round((A * 4 / (2 * math.pi))**2, 2)


# codewars task best solution
import math


def square_area(A):
    side = A * 2 / math.pi  # side = radius
    return round(side**2, 2)


# codewars task best solution
import math


def square_area(A):
    circum = A * 4
    radius = circum / math.pi / 2

    return round((radius**2), 2)


# codewars task best solution
from math import pi


def square_area(a):
    return round((2 * a / pi)**2, 2)
