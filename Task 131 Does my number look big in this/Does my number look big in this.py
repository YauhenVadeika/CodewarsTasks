# my task solution
def narcissistic(value):
    if sum([int(i)**len(str(value)) for i in str(value)]) == value:
        return True
    return False


print(narcissistic(153))
print(narcissistic(1652))


# codewars task best solution
def narcissistic(value):
    return value == sum(int(x)**len(str(value)) for x in str(value))


# codewars task best solution
def narcissistic(value):
    return bool(value == sum([int(a)**len(str(value)) for a in str(value)]))


# codewars task best solution
def narcissistic(value):
    value = str(value)
    size = len(value)
    sum = 0
    for i in value:
        sum += int(i)**size
    return sum == int(value)


# codewars task best solution
def narcissistic(value):
    digs = map(int, str(value))
    l = len(digs)
    return value == sum(map(lambda x: x**l, digs))