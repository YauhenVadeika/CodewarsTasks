# my task solution
def to_binary(n):
    sr = []
    while n:
        sr.append(n % 2)
        n = n // 2
    return int("".join(map(str, sr[::-1])))


print(to_binary(1))
print(to_binary(2))
print(to_binary(3))
print(to_binary(5))
print(to_binary(11))


# codewars task best solution
def to_binary(n):
    return int(f'{n:b}')


# codewars task best solution
def to_binary(n):
    return int(bin(n)[2:])


# codewars task best solution
def to_binary(n):
    return int(bin(n)[2:])


# codewars task best solution
def to_binary(n):
    return int(format(n, 'b'))


# codewars task best solution
to_binary = lambda n: int(str(bin(n))[2:])

