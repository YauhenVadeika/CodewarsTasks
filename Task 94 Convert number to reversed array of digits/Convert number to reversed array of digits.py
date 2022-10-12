# my task solution
def digitize(n):
    return [int(i) for i in reversed(str(n))]


print(digitize(35231))
print(digitize(0))
print(digitize(23582357))
print(digitize(984764738))
print(digitize(45762893920))
print(digitize(548702838394))


# my task solution
def digitize(n):
    return [int(i) for i in str(n)][::-1]


print(digitize(35231))
print(digitize(0))
print(digitize(23582357))
print(digitize(984764738))
print(digitize(45762893920))
print(digitize(548702838394))


# codewars task best solution
def digitize(n):
    return map(int, str(n)[::-1])


# codewars task best solution
def digitize(n):
    result = []
    while n >= 1:
        result.append(n % 10)
        n //= 10
    return result
