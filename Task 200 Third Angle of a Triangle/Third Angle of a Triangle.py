# my task solution
def other_angle(a, b):
    return 180 - (a + b)


print(other_angle(30, 60))
print(other_angle(60, 60))
print(other_angle(43, 78))
print(other_angle(10, 20))


# codewars task best solution
def other_angle(a, b):
    return 180 - a - b


# codewars task best solution
def other_angle(a, b):
    if (a or b) < 0:
        return "angle cannot be smaller than 0"

    else:
        return 180 - (a + b)


# codewars task best solution
other_angle = lambda a, b: 180 - (a + b)


# codewars task best solution
def other_angle(a: int, b: int) -> int:
    """Return the 3rd angle of a triangle."""
    return 180 - a - b


# codewars task best solution
def other_angle(a, b):
    return 180 - a - b if a + b < 180 else 0