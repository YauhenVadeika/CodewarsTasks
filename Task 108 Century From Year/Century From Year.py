# my task solution
def century(year):
    return (year + 99) // 100


print(century(1705))
print(century(1900))
print(century(1902))
print(century(101))
print(century(89))
print(century(1))

# codewars task best solution
import math


def century(year):
    return math.ceil(year / 100)


# codewars task best solution
def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1


# codewars task best solution
def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1


# codewars task best solution
def century(year):
    return (year - 1) // 100 + 1