# my task solution
def min_value(digits):
    return int("".join((map(str, sorted(list(set(digits)))))))


print(min_value([1, 3, 1]))
print(min_value([4, 7, 5, 7]))
print(min_value([4, 8, 1, 4]))

# codewars task best solution
minValue = lambda a: int(''.join(sorted(str(c) for c in set(a))))


# codewars task best solution
def min_value(digits):
    return int("".join(str(x) for x in sorted(set(digits))))


# codewars task best solution
def minValue(arr):
    n = 0
    for i in sorted(set(arr)):
        n *= 10
        n += i
    return n


# codewars task best solution
def minValue(ar):
    return int(''.join(map(str, sorted(set(ar)))))


# codewars task best solution
def min_value(digits):
    l = list(set(digits))
    l.sort(reverse=True)
    return sum(x * 10**i for i, x in enumerate(l))


# codewars task best solution
def Remove(duplicate):
    result = []
    for num in duplicate:
        if num not in result:
            result.append(num)
    return result


def min_value(digits):
    digits = Remove(digits)
    digits = sorted(digits)
    min = ''
    for i in digits:
        min += str(i)
    return int(min)


# codewars task best solution
def minValue(ar):
    good_ar = sorted(list(set(ar)))
    return int(''.join(str(e) for e in good_ar))


# codewars task best solution
def min_value(digits):
    return int("".join(str(i) for i in sorted(set(digits), reverse=False)))


# codewars task best solution
def min_value(digits):
    x = map(str, sorted(set(digits)))
    return int("".join(x))