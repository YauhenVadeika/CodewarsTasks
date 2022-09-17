# my task solution
def divisors(n):
    i = 1
    a = []
    while i * i <= n:
        if n % i == 0:
            a.append(i)
            if i != n // i:
                a.append(n // i)
        i += 1
    return len(a)


print(divisors(4096))
print(divisors(30))
print(divisors(1))


# codewars task best solution
def divisors(n):
    return len([l_div for l_div in range(1, n + 1) if n % l_div == 0])


# codewars task best solution

# For Beginners.

# Time: 11724ms
# it's slow because use isinstance
def divisors5(n):
    return len(list(filter(lambda e: isinstance(e, int), [x if n % x == 0 else None for x in range(1, n + 1)])))


# Time: 7546ms
# it's little fast because just directly check boolean
def divisors4(n):
    return len(list(filter(lambda e: e, [True if n % x == 0 else False for x in range(1, n + 1)])))


# Time: 4731ms
# in python True is evaluate as 1
# so when prime factorization just set True and sum will return count
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


# Time: 3675ms
# even don't need return true, cause comparison operator will return boolean
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


# same time with above but make short code via lambda expression
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])