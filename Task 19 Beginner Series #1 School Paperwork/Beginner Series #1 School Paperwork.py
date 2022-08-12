# my task solution
def paperwork(n, m):
    return 0 if n <= 0 or m <= 0 else n * m


print(paperwork(5, 5))
print(paperwork(-5, 5))
print(paperwork(5, -5))
print(paperwork(-5, -5))
print(paperwork(5, 0))
print(paperwork(0, 0))


# codewars task best solution
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0


# codewars task best solution
def paperwork(n, m):
    if m < 0 or n < 0:
        return 0
    else:
        return n * m


# codewars task best solution
def paperwork(n, m):
    return n * m if n >= 0 and m >= 0 else 0
