"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def max_sequence(arr):

    # Kadane’s Algorithm

    startind = 0
    currsum = 0
    endsum = 0

    for i in range(startind, len(arr)):
        currsum += arr[i]
        if currsum < 0:
            currsum = 0
            startind = i + 1
        if currsum > endsum:
            endsum = currsum
    return endsum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


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


# codewars task best solution
def maxSequence(arr):
    current = 0
    max_found = 0

    for value in arr:
        current += value
        if current < 0:
            current = 0

        if current > max_found:
            max_found = current

    return max_found


# codewars task best solution
def maxSequence(arr):
    # ...
    cur_sum, max_sum = 0, 0
    for item in arr:
        cur_sum = max(item, cur_sum + item)
        max_sum = max(max_sum, cur_sum)
    return max_sum


# codewars task best solution
def maxSequence(arr):
    maximum, temp = 0, 0
    for v in arr:
        temp = max(temp + v, 0)
        maximum = max(maximum, temp)
    return maximum


# codewars task best solution
def maxSequence(arr):
    m, a, s = 0, 0, 0
    for e in arr:
        s += e
        m = min(s, m)
        a = max(a, s - m)
    return a
