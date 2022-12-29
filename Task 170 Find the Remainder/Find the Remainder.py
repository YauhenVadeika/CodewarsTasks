# my task solution
def remainder(a, b):
    try:
        return a % b if a > b else b % a
    except (ZeroDivisionError):
        return


print(remainder(17, 5))
print(remainder(72, 13))
print(remainder(0, -1))
print(remainder(0, 1))
print(remainder(0, 0))


# codewars task best solution
def remainder(a, b):
    if min(a, b) == 0:
        return None
    elif a > b:
        return a % b
    else:
        return b % a


# codewars task best solution
def remainder(a, b):
    if min(a, b) != 0: return max(a, b) % min(a, b)


# codewars task best solution
def remainder(a, b):
    return max(a, b) % min(a, b) if min(a, b) else None


# codewars task best solution
def remainder(a: int, b: int) -> int:
    '''Returns remainder of the larger of two numbers 
    being divided by the smaller of two numbers.
    Returns None for divide by zero.'''
    try:
        return max(a, b) % min(a, b)
    except ZeroDivisionError:
        return None


# codewars task best solution
def remainder(a,b):
    return None if min(a, b) == 0 else max(a, b) % min(a, b)