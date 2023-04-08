"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def basic_op(operator, value1, value2):
    hashtab = {
        '+': value1 + value2,
        '-': value1 - value2,
        '*': value1 * value2,
        '/': value1 / value2
    }
    return hashtab[operator]


print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))


# codewars task best solution
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '/':
        return value1 / value2
    if operator == '*':
        return value1 * value2


# codewars task best solution
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


# codewars task best solution
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))


# codewars task best solution
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')


# codewars task best solution
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        print("Unrecognized Operator. Abort.")


# codewars task best solution
def basic_op(o, a, b):
    return {'+': a + b, '-': a - b, '*': a * b, '/': a / b}.get(o)
