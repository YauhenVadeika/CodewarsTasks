"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def xo(s):
    return s.lower().count("x") == s.lower().count("o")


print(xo('xo'))
print(xo('xxxoo'))
print(xo('xo0'))


# codewars task best solution
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


# codewars task best solution
def xo(s):
    return s.lower().count('x') == s.lower().count('o')


# codewars task best solution
def xo(s):

    exes = 0
    ohs = 0

    for c in s.lower():
        if c == 'x':
            exes += 1
        elif c == 'o':
            ohs += 1

    return exes == ohs


# codewars task best solution
from collections import Counter


def xo(s):
    d = Counter(s.lower())
    return d.get('x', 0) == d.get('o', 0)


# codewars task best solution
def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') else False


# codewars task best solution
def xo(s):
    return s.lower().count("x") is s.lower().count("o")
