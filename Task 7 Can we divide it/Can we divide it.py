# my task solution
def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False


print(is_divide_by(8, 2, 4))
print(is_divide_by(12, -3, 4))
print(is_divide_by(48, 2, -5))


# my task solution
def is_divide_by(number, a, b):
    return True if number % a == 0 and number % b == 0 else False


print(is_divide_by(8, 2, 4))
print(is_divide_by(12, -3, 4))
print(is_divide_by(48, 2, -5))


# codewars task best solution
def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0


# codewars task best solution
def is_divide_by(n, a, b):
    return n % a == 0 == n % b
