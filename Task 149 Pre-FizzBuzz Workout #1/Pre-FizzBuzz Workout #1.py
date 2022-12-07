# my task solution
def pre_fizz(n):
    return [n for n in range(1, n + 1)]


print(pre_fizz(1))
print(pre_fizz(2))
print(pre_fizz(3))
print(pre_fizz(4))
print(pre_fizz(5))


# codewars task best solution
def pre_fizz(n):
    return list(range(1, n + 1))


# codewars task best solution
pre_fizz = lambda n: list(range(1, n + 1))


# codewars task best solution
def pre_fizz(n):
    return [i + 1 for i in range(n)]


# codewars task best solution
def pre_fizz(n):
    mas = []
    for i in range(1, n + 1):
        mas.append(i)
    return mas