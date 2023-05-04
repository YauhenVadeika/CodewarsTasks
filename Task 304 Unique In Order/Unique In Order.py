"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def unique_in_order(sequence):

    return [
        sequence[i] for i in range(len(sequence))
        if sequence[i - 1] != sequence[i] or i == 0
    ]


print(unique_in_order(["A"]))
print(unique_in_order("AA"))
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order(""))
print(unique_in_order([]))


# codewars task best solution
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


# codewars task best solution
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res


# codewars task best solution
from itertools import groupby


def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]


# codewars task best solution
unique_in_order = lambda l: [
    z for i, z in enumerate(l) if i == 0 or l[i - 1] != z
]


# codewars task best solution
def unique_in_order(iterable):
    return [
        ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1]
    ]
