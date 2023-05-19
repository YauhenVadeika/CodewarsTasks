"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def productFib(prod):

    x = 0
    y = 1

    while x * y < prod:
        x, y = y, (x + y)
        # print(x, end=" \n")
        # print(y, end=" ")
    return [x, y, prod == (x * y)]


# print(productFib(0))
# print(productFib(1))
# print(productFib(2))
# print(productFib(4895))
print(productFib(5895))


# codewars task best solution
def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]


# codewars task best solution


# codewars task best solution
def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, b + a
    return [a, b, a * b == prod]


# codewars task best solution
def productFib(prod):
    func = lambda a, b: func(b, a + b
                             ) if a * b < prod else [a, b, a * b == prod]
    return func(0, 1)


# codewars task best solution
def productFib(prod):
    a, b = 0, 1
    rez = 0
    while rez < prod:
        a, b = b, a + b
        rez = a * b
    return [a, b, rez == prod]


# codewars task best solution
class Fib(object):
    """docstring for Fib"""

    def __init__(self):
        super(Fib, self).__init__()
        self._a = 0
        self._b = 1

    def __call__(self):
        self._a, self._b = self._b, self._a + self._b
        return self._a, self._b


def productFib(prod):
    # your code
    fib = Fib()
    a, b = fib()
    while (a * b) < prod:
        a, b = fib()

    return [a, b, (a * b) == prod]


# codewars task best solution
def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]


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


# codewars task best solution
def productFib(prod, f1=0, f2=1):
    return [f1, f2, True] if prod == f1 * f2 else [
        f1, f2, False
    ] if prod < f1 * f2 else productFib(prod, f2, f1 + f2)
