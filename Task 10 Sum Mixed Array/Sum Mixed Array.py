# my task solution
def sum_mix(arr):
    summa = 0
    for i in (arr):
        var = int(i)
        summa += var
    return summa


print(sum_mix([9, 3, '7', '3']))
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))


# my task solution
def sum_mix(arr):
    res = [int(i) for i in arr]
    return sum(res)


print(sum_mix([9, 3, '7', '3']))
print(sum_mix([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]))


# codewars task best solution
def sum_mix(arr):
    return sum(map(int, arr))


# codewars task best solution
def sum_mix(arr):
    return sum(int(n) for n in arr)
