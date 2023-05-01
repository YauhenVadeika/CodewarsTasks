"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def find_uniq(arr):

    for i in set(arr):
        if arr.count(i) == 1:
            return i


print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3]))


# codewars task best solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


# codewars task best solution
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e


# codewars task best solution
def find_uniq(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]


# codewars task best solution
from collections import Counter


def find_uniq(a):
    return Counter(a).most_common()[-1][0]


# codewars task best solution
def find_uniq(arr):
    if arr[0] != arr[1]:
        if arr[0] != arr[2]:
            return arr[0]
        else:
            return arr[1]
    else:
        for i in arr[2:]:
            if i != arr[0]:
                return i


# codewars task best solution
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]