# my task solution
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))


# codewars task best solution
def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1


# codewars task best solution
def find_even_index(arr):
    left, right = 0, sum(arr)
    for i, e in enumerate(arr):
        right -= e
        if left == right:
            return i
        left += e
    return -1


# codewars task best solution
def find_even_index(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i + 1:])]
    return r[0] if r else -1


# codewars task best solution
def find_even_index(arr):

    def partial_sum(arr):
        total = 0
        for i in arr:
            total += i
            yield total

    sums = list(partial_sum(arr))

    def sumleft(i):
        if i != 0:
            return sums[i - 1]
        else:
            return 0

    def sumright(i):
        return sums[len(sums) - 1] - sums[i]

    for i in range(len(arr)):
        sl = sumleft(i)
        sr = sumright(i)
        if sl == sr:
            return i
    return -1


# codewars task best solution
def find_even_index(arr):
    return res[0] if (res := [
        x for x in range(0, len(arr)) if sum(arr[:x]) == sum(arr[x + 1:])
    ]) else -1
