# my task solution
def series_sum(n):
    return '{:.2f}'.format(sum(1 / (1 + i * 3) for i in range(n)))


print(series_sum(3))


# codewars task best solution
def series_sum(n):
    return '{:.2f}'.format(sum(1.0 / (3 * i + 1) for i in range(n)))


# codewars task best solution
def series_sum(n):
    sum = 0.0
    for i in range(0, n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum
