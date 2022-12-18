# my task solution
def two_sum(numbers, target):
    hash = {}
    for i, j in enumerate(numbers):
        x = target - j
        if x in hash:
            return [hash[x], i]
        hash[j] = i


print(two_sum([1, 2, 3], 4))
print(two_sum([1234, 5678, 9012], 14690))


# codewars task best solution
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]


# codewars task best solution
def two_sum(n, target):
    for i in range(len(n) - 1):
        if (target - n[i]) in n[i + 1:]:
            return [i, n[i + 1:].index(target - n[i]) + (i + 1)]
    return None


# codewars task best solution
from itertools import combinations as comb


def two_sum(numbers, target):
    for (ia, a), (ib, b) in comb(enumerate(numbers), 2):
        if a + b == target:
            return [ia, ib]


# codewars task best solution
def two_sum(numbers, target):
    z = 0
    zoo = []
    for n in numbers:
        complement = target - numbers[z]
        z += 1
        j = 1 + n
        for j in numbers:
            if j == complement:
                zoo.append(numbers.index(n))
                if numbers.index(n) == numbers.index(j):
                    zoo.append(1)
                else:
                    zoo.append(numbers.index(j))

                return zoo