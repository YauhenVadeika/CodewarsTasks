# my task solution
import math


def approx_equals(a, b):
    return math.isclose(a, b, abs_tol=0.001)


print(approx_equals(175.9827, 82.25))
print(approx_equals(-156.24037, -156.24038))


# codewars task best solution
def approx_equals(a, b):
    return abs(a - b) < 0.001


# codewars task best solution
def approx_equals(a, b):
    return abs(a - b) < 1e-3


# codewars task best solution
def approx_equals(a, b):
    a = round(a, 5)
    b = round(b, 5)
    return abs(a - b) <= 0.001


# codewars task best solution
approx_equals = lambda a, b: abs(a - b) < .001
