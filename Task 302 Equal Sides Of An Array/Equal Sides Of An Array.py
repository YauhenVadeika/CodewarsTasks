"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


print(find_even_index([1, 2, 3, 4, 3, 2, 1]))
print(find_even_index([1, 100, 50, -51, 1, 1]))
print(find_even_index([0, 0, 0, 0, 0]))
print(find_even_index(list(range(-100, -1))))


# codewars task best solution
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1


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
    for i in range(len(arr)):
        if sum(arr[i:]) == sum(arr[:i + 1]):
            return i
    return -1


# codewars task best solution
def find_even_index(arr):
    r = [i for i in range(len(arr)) if sum(arr[0:i]) == sum(arr[i + 1:])]
    return r[0] if r else -1


# codewars task best solution
def find_even_index(arr):
    right = sum(arr)
    left = 0
    for i, x in enumerate(arr):
        right -= x
        if right == left:
            return i
        left += x
    return -1


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
    left_sum, right_sum = 0, sum(arr)

    for i, n in enumerate(arr):
        right_sum -= n
        if left_sum == right_sum:
            return i
        left_sum += n

    return -1


# codewars task best solution
def find_even_index(arr):
    left, right = 0, sum(arr)
    for i, v in enumerate(arr):
        right -= v
        if left == right: return i
        left += v
    return -1