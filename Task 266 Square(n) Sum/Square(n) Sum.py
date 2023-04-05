"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def square_sum(numbers):
    return sum(i**2 for i in numbers)


print(square_sum([1, 2]))
print(square_sum([-1, 0, 1]))
print(square_sum([]))


# codewars task best solution
def square_sum(numbers):
    return sum(x**2 for x in numbers)


# codewars task best solution
def square_sum(numbers):
    return sum(x * x for x in numbers)


# codewars task best solution
def square_sum(numbers):
    res = 0
    for num in numbers:
        res = res + num * num
    return res


# codewars task best solution
def square_sum(numbers):
    return sum(map(lambda x: x**2, numbers))


# codewars task best solution
def square_sum(numbers):
    return sum([x**2 for x in numbers])
