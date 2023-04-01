"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def positive_sum(arr):
    return sum(i if i > 0 else 0 for i in arr)


print(positive_sum([1, -2, 3, 4, 5]))
print(positive_sum([-1, -2, -3, -4, -5]))


# codewars task best solution
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# codewars task best solution
def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum


# codewars task best solution
def positive_sum(arr):
    return sum(filter(lambda x: x > 0, arr))


# codewars task best solution
def positive_sum(arr):
    ''' I really hate these one line codes, but here I am...
        trying to be cool here... and writing some'''
    return sum(map(lambda x: x if x > 0 else 0, arr))