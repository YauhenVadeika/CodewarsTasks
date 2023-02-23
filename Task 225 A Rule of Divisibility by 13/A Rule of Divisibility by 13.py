# my task solution
def thirt(n):

    loop = [1, 10, 9, 12, 3, 4]
    sum = 0
    while True:
        current_sum = 0
        for index, digit in enumerate(str(n)[::-1]):
            current_index = index % len(loop)
            current_sum += int(digit) * loop[current_index]
        if sum == current_sum:
            return sum

        sum = current_sum
        n = current_sum


print(thirt(123456789))

# codewars task best solution
array = [1, 10, 9, 12, 3, 4]


def thirt(n):
    total = sum(
        [int(c) * array[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)


# codewars task best solution
import itertools as it


def thirt(n):
    if n < 100: return n

    pattern = it.cycle([1, 10, 9, 12, 3, 4])

    return thirt(sum(d * n for d, n in zip(map(int, str(n)[::-1]), pattern)))


# codewars task best solution
def thirt(n):
    seq = [1, 10, 9, 12, 3, 4]
    s = str(n)
    t = sum(seq[i % 6] * int(s[-i - 1]) for i in range(len(s)))
    return t if t == n else thirt(t)


# codewars task best solution
from itertools import cycle


def thirt(n):
    c = cycle([1, 10, 9, 12, 3, 4])
    m = sum(int(l) * next(c) for l in str(n)[::-1])
    return m if m == n else thirt(m)


# codewars task best solution
def thirt(n):
    ans = sum(
        [int(val) * ((10**key) % 13) for key, val in enumerate(str(n)[::-1])])
    return n if ans == n else thirt(ans)