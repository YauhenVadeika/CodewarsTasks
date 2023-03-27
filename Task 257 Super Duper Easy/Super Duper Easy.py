# my task solution
def problem(a):
    return "Error" if a == str(a) else a * 50 + 6


print(problem(1))
print(problem("hello"))


# codewars task best solution
def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"


# codewars task best solution
def problem(a):
    return "Error" if isinstance(a, str) else a * 50 + 6


# codewars task best solution
def problem(a):
    return "Error" if a == str(a) else a * 50 + 6


# codewars task best solution
def problem(x):
    return (x * 50 + 6) if isinstance(x, (int, float)) else "Error"


# codewars task best solution
def problem(a):
    if isinstance(a, str):
        return "Error"
    else:
        return (a * 50) + 6
