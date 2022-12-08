# my task solution
def xor(a, b):
    return False if a == b else True


print(xor(False, False))
print(xor(True, False))
print(xor(False, True))
print(xor(True, True))


# codewars task best solution
def xor(a, b):
    return a != b


# codewars task best solution
def xor(a, b):
    return a ^ b


# codewars task best solution
def xor(a, b):
    return a is not b


# codewars task best solution
xor = lambda a, b: a != b


# codewars task best solution
def xor(a, b):
    return (a or b) and not (a and b)
