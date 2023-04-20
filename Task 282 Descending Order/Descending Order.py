"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def descending_order(num):
    return int("".join(sorted(list(str(num)), reverse=True)))


print(descending_order(42145))
print(descending_order(145263))
print(descending_order(123456789))


# codewars task best solution
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


# codewars task best solution
def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num), reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')


# codewars task best solution
def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    return int(s)


# codewars task best solution
def Descending_Order(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))


def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))


# codewars task best solution
