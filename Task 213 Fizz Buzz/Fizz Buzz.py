# my task solution
def fizzbuzz(n):

    box = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            box.append('FizzBuzz')
            continue
        if i % 3 == 0:
            box.append('Fizz')
            continue
        if i % 5 == 0:
            box.append('Buzz')
            continue
        else:
            box.append(i)
    return box


print(fizzbuzz(3))
print(fizzbuzz(10))


# codewars task best solution
def fizzbuzz(n):
    return [
        'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i
        for i in range(1, n + 1)
    ]


# codewars task best solution
def fizzify(n):
    if n % 15 == 0: return "FizzBuzz"
    if n % 5 == 0: return "Buzz"
    if n % 3 == 0: return "Fizz"
    return n


def fizzbuzz(n):
    return map(fizzify, range(1, n + 1))


# codewars task best solution
def fizzbuzz(n):
    return [fb(m) for m in range(1, n + 1)]


def fb(m):
    r = (m % 3 == 0) * "Fizz" + (m % 5 == 0) * "Buzz"
    return r if r != "" else m


# codewars task best solution
def fizzbuzz(n):
    out = list()
    for i in range(1, n + 1):
        res = ''
        if i % 3 == 0: res += 'Fizz'
        if i % 5 == 0: res += 'Buzz'
        out.append(i if len(res) == 0 else res)
    return out


# codewars task best solution
def fizzbuzz(n):
    return [('FizzBuzz' if i % 5 == 0 else 'Fizz') if i %
            3 == 0 else 'Buzz' if i % 5 == 0 else i for i in xrange(1, n + 1)]
