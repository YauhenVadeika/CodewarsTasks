# my task solution
def productFib(prod):

    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]


print(productFib((714)))


# codewars task best solution
def productFib(prod):
    func = lambda a, b: func(b, a + b
                             ) if a * b < prod else [a, b, a * b == prod]
    return func(0, 1)


# codewars task best solution
def make_fib(a=1, b=1):
    while True:
        yield (a, b)
        a, b = b, a + b


def productFib(prod):
    for n1, n2 in make_fib():
        if n1 * n2 == prod:
            return [n1, n2, True]
        if n1 * n2 > prod:
            return [n1, n2, False]
