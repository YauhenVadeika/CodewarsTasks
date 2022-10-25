# my task solution
def count_by(x, n):
    return list(range(x, (n + 1) * x, x))


print(count_by(1, 10))
print(count_by(2, 5))
print(count_by(50, 5))
print(count_by(100, 5))


# codewars task best solution
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]


# codewars task best solution
def count_by(x, n):
    arr = []
    for num in range(1, n + 1):
        result = x * num
        arr.append(result)
    return arr
