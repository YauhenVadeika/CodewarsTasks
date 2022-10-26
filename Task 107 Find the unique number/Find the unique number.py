# my task solution
def find_uniq(arr):

    if arr.count(max(arr)) == 1:
        return arr[arr.index(max(arr))]
    else:
        arr.count(min(arr))
        return arr[arr.index(min(arr))]


print(find_uniq([1, 1, 1, -2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))
print(find_uniq([3, 10, 3, 3, 3]))
print(find_uniq([3, 3, 3, 3, 42689.417719596044]))


# codewars task best solution
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


# codewars task best solution
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e


# codewars task best solution
def find_uniq(arr):
    a = sorted(arr)
    return a[0] if a[0] != a[1] else a[-1]


# codewars task best solution
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]


# codewars task best solution
def find_uniq(arr):
    return min(set(arr), key=arr.count)
