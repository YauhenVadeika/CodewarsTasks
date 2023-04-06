"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def summation(num):
    return sum(list(range(num + 1)))


print(summation(8))
print(summation(100))
print(summation(213))
print(summation(0))


# codewars task best solution
def summation(num):
    return sum(xrange(num + 1))


# codewars task best solution
def summation(num):
    return (1 + num) * num / 2


# codewars task best solution
def summation(num):
    return sum(range(1, num + 1))


# codewars task best solution
def summation(num):
    return sum(range(num + 1))


# codewars task best solution
def summation(num):
    total = 0
    for i in range(0, num + 1):
        total = total + i
    return total


# codewars task best solution
def summation(num):
    return num * (num + 1) // 2
