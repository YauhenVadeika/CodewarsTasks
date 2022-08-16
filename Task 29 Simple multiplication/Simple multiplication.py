# my task solution
def simple_multiplication(number):
    return (number * 8) if (number % 2) == 0 else (number * 9)


print(simple_multiplication(2))
print(simple_multiplication(1))
print(simple_multiplication(8))
print(simple_multiplication(4))
print(simple_multiplication(5))


# codewars task best solution
def simple_multiplication(number):
    return number * 9 if number % 2 else number * 8


# codewars task best solution
def simple_multiplication(n):
    return n * (8 + n % 2)
