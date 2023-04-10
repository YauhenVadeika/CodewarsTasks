"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def square_digits(num):
    return int("".join([str(i**2) for i in list(map(int, (str(num))))]))


print(square_digits(9119))
print(square_digits(0))


# codewars task best solution
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)


# codewars task best solution
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))


# codewars task best solution
def square_digits(num):
    num = str(num)
    ans = ''
    for i in num:
        ans += str(int(i)**2)
    return int(ans)


# codewars task best solution
def square_digits(num):
    return int(''.join(str(int(c)**2) for c in str(num)))


# codewars task best solution
def square_digits(num):
    squares = ''
    for x in str(num):
        squares += str(int(x)**2)
    return int(squares)