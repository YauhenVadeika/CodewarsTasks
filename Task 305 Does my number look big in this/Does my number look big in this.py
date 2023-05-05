"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def narcissistic(value):
    return True if sum([int(i)**len(str(value))
                        for i in str(value)]) == value else False


print(narcissistic(371))
print(narcissistic(122))


# codewars task best solution
def narcissistic(value):
    return value == sum(int(x)**len(str(value)) for x in str(value))


# codewars task best solution
def narcissistic(value):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i)**size
    return sum == int(value)


# codewars task best solution
def narcissistic(value):
    return bool(value == sum([int(a)**len(str(value)) for a in str(value)]))


# codewars task best solution
def narcissistic(value):
    string = str(value)
    length = len(string)
    sum_of_i = 0
    for i in string:
        sum_of_i += int(i)**length
    if sum_of_i == value:
        result = True
    else:
        result = False
    return result


# codewars task best solution
def narcissistic(value):
    vstr = str(value)
    nvalue = sum(int(i)**len(vstr) for i in vstr)
    return nvalue == value


# codewars task best solution
def narcissistic(value):
    return value == sum(int(i)**len(str(value)) for i in str(value))


# codewars task best solution
narcissistic = lambda n: sum([int(d)**len(str(n)) for d in list(str(n))]) == n
