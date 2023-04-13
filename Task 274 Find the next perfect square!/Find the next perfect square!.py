"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def find_next_square(sq):
    return int(2 *
               (sq**0.5)) + (1 + sq) if sq**0.5 == round(sq**0.5, 1) else -1


print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(15241383936))
print(find_next_square(114))


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


# codewars task best solution
from math import sqrt


def find_next_square(sq):

    if int(sqrt(sq)) == sqrt(sq):
        return (sqrt(sq) + 1)**2
    else:
        return -1
