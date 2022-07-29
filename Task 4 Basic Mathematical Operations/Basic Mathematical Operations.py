# my task solution
def basic_op(operator, value1, value2):
    if operator == '+':
        res = value1 + value2
    if operator == '-':
        res = value1 - value2
    if operator == '*':
        res = value1 * value2
    if operator == '/':
        res = value1 / value2
    return res


# print(basic_op('+', 4, 7))
# print(basic_op('-', 15, 18))
# print(basic_op('*', 5, 5))
# print(basic_op('/', 49, 7))


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
