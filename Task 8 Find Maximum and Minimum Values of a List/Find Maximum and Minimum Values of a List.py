# my task solution
def minimum(arr):
    return min(arr)


print(minimum([4, 6, 2, 1, 9, 63, -134, 566]))


def maximum(arr):
    return max(arr)


print(maximum([4, 6, 2, 1, 9, 63, -134, 566]))


# codewars task best solution
def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


# codewars task best solution
def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low


def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high