# my task solution
def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if i != j:
            return j


print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
print(first_non_consecutive([-5, -4, -3, -1]))


# codewars task best solution
def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]


# codewars task best solution
def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None