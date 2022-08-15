# my task solution
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


print(is_triangle(1, 2, 2))
print(is_triangle(7, 2, 2))
print(is_triangle(1, 2, 3))


# codewars task best solution
def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)


# codewars task best solution
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c