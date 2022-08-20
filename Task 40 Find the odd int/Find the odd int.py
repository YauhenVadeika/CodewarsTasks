# my task solution
def find_it(seq):
    a = min(seq)
    b = max(seq)
    for i in range(a, b + 1, 1):
        if i in seq:
            c = seq.count(i)
            if c % 2 != 0:
                return i


print(find_it([0]))
print(find_it([7]))
print(find_it([3, 3, 0, 1, 0, 1, 0]))
print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


# codewars task best solution
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


# codewars task best solution
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]


# codewars task best solution
import operator


def find_it(xs):
    return reduce(operator.xor, xs)