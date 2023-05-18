"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def scramble(s1, s2):

    for var in set(s2):
        if s2.count(var) > s1.count(var):
            return False
    return True


print(scramble('rkqodlw', 'world'))
print(scramble('katas', 'steak'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble("gcuejcujwolpdxie", "cgwjwluc"))

# codewars task best solution
from collections import Counter


def scramble(s1, s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2) - Counter(s1)) == 0


# codewars task best solution
def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))


# codewars task best solution
def scramble(s1, s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True


# codewars task best solution
def scramble(s1, s2):
    return all(s1.count(x) >= s2.count(x) for x in set(s2))


# codewars task best solution
def scramble(s1, s2):
    dct = {}
    for l in s1:
        if l not in dct:
            dct[l] = 1
        else:
            dct[l] += 1
    for l in s2:
        if l not in dct or dct[l] < 1:
            return False
        else:
            dct[l] -= 1
    return True


# codewars task best solution
def scramble(s1, s2):
    h = [0] * 26
    for c in s1:
        h[ord(c) - 97] += 1
    for c in s2:
        h[ord(c) - 97] -= 1
    return 0 == sum(n < 0 for n in h)


# codewars task best solution
from collections import Counter


def scramble(s1, s2):
    return not (Counter(s2) - Counter(s1))


# codewars task best solution
from collections import Counter


def scramble(s1, s2):
    # Python 3.10 rich comparison operators for Counter ftw!
    return Counter(s2) <= Counter(s1)