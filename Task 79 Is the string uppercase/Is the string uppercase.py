# my task solution
import re


def is_uppercase(inp):

    if inp.upper() == inp:
        return True
    elif re.match('[a-z]', inp) is not None:
        return False
    else:
        return False


print(is_uppercase("hello I AM DONALD"))
print(is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ"))
print(is_uppercase("HELLO I AM DONALD"))
print(is_uppercase("$%&"))


# codewars task best solution
def is_uppercase(inp):
    return inp.upper() == inp


# codewars task best solution
def is_uppercase(inp):
    for letter in inp:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True

# codewars task best solution
def is_uppercase(stg):
    return not any(c.islower() for c in stg)
