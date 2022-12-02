# my task solution
def repeat_str(repeat, string):
    return repeat * string


print(repeat_str(4, 'a'))

# codewars task best solution
repeat_str = lambda r, s: s * r


# codewars task best solution
def repeat_str(repeat, string):
    return "".join([string] * repeat)
