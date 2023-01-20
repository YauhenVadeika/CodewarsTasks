# my task solution
def sum_of_differences(arr):
    arr.sort(reverse=True)
    s = 0
    for i in range(1, len(arr)):
        s += arr[i - 1] - arr[i]
    return s

print(sum_of_differences([2, 1, 10]))


# codewars task best solution
def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0


# codewars task best solution
def sum_of_differences(arr):
    arr.sort(reverse=True)
    i = 0
    res = 0
    while i < len(arr) - 1:
        res += arr[i] - arr[i + 1]
        i += 1
    return res


# codewars task best solution
def sum_of_differences(arr):
    arr = sorted(arr, reverse=True)
    return sum(a - b for a, b in zip(arr, arr[1:]))


# codewars task best solution
def sum_of_differences(arr):
    return max(arr or [0]) - min(arr or [0])


# codewars task best solution
def sum_of_differences(arr):
    return abs(sum(i - j for i, j in zip(sorted(arr), sorted(arr)[1:])))
