# my task solution
def get_sum(a, b):
    if a == b:
        return a
    summ = 0
    for n in range(min(a, b), max(a, b) + 1):
        summ += n
    return summ


print(get_sum(1, 0))
print(get_sum(1, 2))
print(get_sum(0, 1))
print(get_sum(1, 1))
print(get_sum(-1, 0))
print(get_sum(-1, 2))


# codewars task best solution
def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


# codewars task best solution
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2


# codewars task best solution
def get_sum(a, b):
    soma = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a + 1):
            soma += i
        return soma
    else:
        for i in range(a, b + 1):
            soma += i
        return soma