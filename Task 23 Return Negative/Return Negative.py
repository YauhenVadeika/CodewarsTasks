# my task solution
def make_negative(number):
    return number * (-1) if number > 0 else number


print(make_negative(1))
print(make_negative(-5))
print(make_negative(0))


# codewars task best solution
def make_negative(number):
    return -abs(number)


# codewars task best solution
def make_negative(number):
    return -number if number > 0 else number


# codewars task best solution
def make_negative(number):
    return (-1) * abs(number)