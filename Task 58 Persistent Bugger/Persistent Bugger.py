# my task solution
def persistence(n):
    if n < 10:
        return 0
    num = str(n)
    res = 1
    for i in num:
        res = res * int(i)
    return 1 + persistence(res)


print(persistence(39))
print(persistence(4))
print(persistence(25))

# codewars task best solution
import operator


def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i


# codewars task best solution
def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


# codewars task best solution
def persistence(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist