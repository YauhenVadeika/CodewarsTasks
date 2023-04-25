"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def is_square(n):
    return n == (n**0.5)**2


print(is_square(4))
print(is_square(3))

# codewars task best solution
import math


def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0


# codewars task best solution
def is_square(n):
    return n >= 0 and (n**0.5) % 1 == 0


# codewars task best solution
import math


def is_square(n):

    if n < 0:
        return False

    sqrt = math.sqrt(n)

    return sqrt.is_integer()


# codewars task best solution
import math


def is_square(n):
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False


# codewars task best solution
def is_square(n):
    if n >= 0:
        if int(n**.5)**2 == n:
            return True
    return False


# codewars task best solution
from math import sqrt


def is_square(n):
    return n >= 0 and sqrt(n).is_integer()
