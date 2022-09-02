# my task solution
def stray(arr):
    return [num for num in arr if arr.count(num) == 1][0]


arr = [1, 1, 2]
print(stray(arr))


# codewars task best solution
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x


# codewars task best solution
def stray(arr):
    return min(arr, key=arr.count)


# codewars task best solution
def stray(arr):
    for x in set(arr):
        if arr.count(x) == 1: return x
