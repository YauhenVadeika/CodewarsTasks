"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


print(odd_or_even([0, 1, 2]))
print(odd_or_even([0, 1, 3]))
print(odd_or_even([0]))
print(odd_or_even([0, -1, -5]))


# codewars task best solution
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


# codewars task best solution
def oddOrEven(arr):
    return "odd" if sum(arr) % 2 else "even"


# codewars task best solution
def oddOrEven(arr):
    """determine whether a given list of numbers is odd or even"""
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"


# codewars task best solution
def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]


# codewars task best solution
def oddOrEven(arr):
    c = 0
    for i in arr:
        c += i
    if c % 2 == 0:
        return 'even'
    else:
        return 'odd'
