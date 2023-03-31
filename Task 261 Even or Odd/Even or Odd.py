"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


print(even_or_odd(2))
print(even_or_odd(1))
print(even_or_odd(0))


# codewars task best solution
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'


# codewars task best solution
def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'


# codewars task best solution
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# codewars task best solution
def even_or_odd(number):
    return ["Even", "Odd"][number % 2]


# codewars task best solution
def even_or_odd(number):
    # number % 2 will return 0 for even numbers and 1 for odd ones.
    # 0 evaluates to False and 1 to True, so we can do it with one line
    return "Odd" if number % 2 else "Even"


# codewars task best solution
def even_or_odd(number):
    status = ""
    if number % 2 == 0:
        status = "Even"
    else:
        status = "Odd"

    return status
