"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def make_negative(number):
    return -number if number > 0 else number


print(make_negative(42))
print(make_negative(-42))
print(make_negative(0))


# codewars task best solution
def make_negative(number):
    return -abs(number)


# codewars task best solution
def make_negative(number):
    return -number if number > 0 else number


# codewars task best solution
def make_negative(number):
    return (-1) * abs(number)


# codewars task best solution
def make_negative(number):
    # return negative of number. BUT: negative in = negative out. zero remains zero
    return -abs(number)
