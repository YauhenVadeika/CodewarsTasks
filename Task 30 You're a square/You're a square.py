# my task solution
def is_square(n):
    return True if n >= 0 and (n**0.5).is_integer() else False


print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))

# codewars task best solution
import math


def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0


# codewars task best solution
import math


def is_square(n):

    if n < 0:
        return False

    sqrt = math.sqrt(n)

    return sqrt.is_integer()