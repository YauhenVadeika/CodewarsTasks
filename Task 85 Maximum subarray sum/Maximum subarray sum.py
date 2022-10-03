# my task solution
def maxSequence(arr):
    maximum = 0
    local_maximum = 0
    for i in arr:
        if local_maximum > 0:
            local_maximum += i
            if local_maximum < 0:
                local_maximum = 0
            elif local_maximum > maximum:
                maximum = local_maximum
        elif i > 0:
            local_maximum += i

    return maximum


print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# codewars task best solution
def maxSequence(arr):
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0: curr = 0
        if curr > max: max = curr
    return max


# codewars task best solution
def maxSequence(arr):
    maxl = 0
    maxg = 0
    for n in arr:
        maxl = max(0, maxl + n)
        maxg = max(maxg, maxl)
    return maxg


# codewars task best solution
def maxSequence(arr):
    lowest = ans = total = 0
    for i in arr:
        total += i
        lowest = min(lowest, total)
        ans = max(ans, total - lowest)
    return ans