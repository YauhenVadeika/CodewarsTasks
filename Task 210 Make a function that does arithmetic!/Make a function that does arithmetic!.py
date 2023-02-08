# my task solution
def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    if operator == "subtract":
        return a - b
    if operator == "multiply":
        return a * b
    if operator == "divide":
        return a / b


print(arithmetic(1, 2, "add"))
print(arithmetic(8, 2, "subtract"))
print(arithmetic(5, 2, "multiply"))
print(arithmetic(8, 2, "divide"))


# codewars task best solution
def arithmetic(a, b, operator):
    return {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b,
    }[operator]


# codewars task best solution
from operator import add, mul, sub, truediv


def arithmetic(a, b, operator):
    ops = {'add': add, 'subtract': sub, 'multiply': mul, 'divide': truediv}
    return ops[operator](a, b)


# codewars task best solution
import operator


def arithmetic(a, b, operator_name):
    operators = {
        "add": operator.add,
        "subtract": operator.sub,
        "multiply": operator.mul,
        "divide": operator.truediv
    }
    return operators[operator_name](a, b)


# codewars task best solution
def arithmetic(a, b, operator):
    return a + b if operator == 'add' else a - b if operator == 'subtract' else a * b if operator == 'multiply' else a / b


# codewars task best solution
def arithmetic(a, b, operator):
    op = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
    return eval("{} {} {}".format(a, op[operator], b))