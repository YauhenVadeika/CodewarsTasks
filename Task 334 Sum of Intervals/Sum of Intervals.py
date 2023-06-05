"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def sum_of_intervals(intervals):

    srt = sorted(intervals)
    # print(srt)
    mx = srt[0][0]
    mix = 0
    # print(mx, mix)
    for i in range(len(srt)):
        mix += max(srt[i][1], mx) - max(srt[i][0], mx)
        mx = max(mx, srt[i][1])
    return mix


print(sum_of_intervals([[1, 2], [6, 10], [11, 15]]))
print(sum_of_intervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]))
print(sum_of_intervals([[0, 20], [-100000000, 10], [30, 40]]))


# codewars task best solution
def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a, b in sorted(intervals):
        if top < a: top = a
        if top < b: s, top = s + b - top, b
    return s


# codewars task best solution
def sum_of_intervals(intervals):
    intervals.sort()
    lim, res = intervals[0][0], 0
    for i in range(len(intervals)):
        res += max(intervals[i][1], lim) - max(intervals[i][0], lim)
        lim = max(lim, intervals[i][1])
    return res


# codewars task best solution
def sum_of_intervals(intervals):
    intervals.sort()
    end, subtract = intervals[0][1], 0
    for i in intervals:
        if i[0] > end: subtract += i[0] - end
        if i[1] > end: end = i[1]
    return end - subtract - intervals[0][0]


# codewars task best solution
def sum_of_intervals(intervals):

    output = []

    # We turn our list of tuples into a list of lists
    list_of_lists = [list(x) for x in intervals]

    # We now sort the list in ascending order, according the first element in each list
    list_of_lists.sort()
    print(f" list of lists {list_of_lists}")

    # Get rid of duplicate elements
    # res will be our list without duplicates
    res = []
    [res.append(x) for x in list_of_lists if x not in res]
    print(f"res {res}")
    # We now deal with exceptions

    if len(res) < 1:
        return []
    if len(res) == 1:
        answer = res[0][1] - res[0][0]
        print(answer)
        return answer

    # Store the first interval in our list as  a variable and append it to an empty list

    interval_to_be_treated = res[0]
    output.append(interval_to_be_treated)
    # This is the clever bit. It loops through res and stores the next interval start and end values in two variables
    for i in range(len(res)):
        # We set a variable upper_limit to be the upper limit of the interval in the first element in res
        upper_limit = interval_to_be_treated[1]
        print(f"upper limit is {upper_limit}")
        # We create two variables, low_res stores the lower limit of an interval and upper_res the upper limit
        low_res = res[i][0]
        upper_res = res[i][1]
        # This is the clever bit. Check that the end value of the upper limit current2 variable is greater than or equal to the start value
        # of the next interval
        # if true, change the end value of current2 to be the max of the current end interval
        if upper_limit >= low_res:
            interval_to_be_treated[1] = max(upper_limit, upper_res)
            print(f" interval_to_be_treated[1] {interval_to_be_treated[1]}")

        else:
            # else change the value held in the current variable to be current interval in res
            interval_to_be_treated = res[i]

            output.append(interval_to_be_treated)

    print(f" output {output}")

    # We now need to iterate through output to get the lengths of the ranges
    range_value = 0
    for m in range(len(output)):
        range_value = range_value + (output[m][1] - output[m][0])
    print(f"range value {range_value}")

    return range_value


# codewars task best solution
def sum_of_intervals(intervals):
    intervals.sort()
    x = 0
    while x < len(intervals) - 1:
        if intervals[x][0] <= intervals[
                x + 1][0] and intervals[x][1] >= intervals[x + 1][1]:
            intervals.pop(x + 1)
        elif intervals[x][0] <= intervals[
                x + 1][0] and intervals[x][1] >= intervals[
                    x + 1][0] and intervals[x][1] < intervals[x + 1][1]:
            intervals[x] = (intervals[x][0], intervals[x + 1][1])
            intervals.pop(x + 1)
        else:
            x += 1

    return sum(intervals[x][1] - intervals[x][0]
               for x in range(len(intervals)))


# codewars task best solution
def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    initial = 0
    currentStart, currentEnd = intervals[0]

    for start, end in intervals[1:]:
        if start <= currentEnd:
            currentEnd = max(currentEnd, end)
        else:
            initial += currentEnd - currentStart
            currentStart, currentEnd = start, end

    initial += currentEnd - currentStart
    return initial


# codewars task best solution
from operator import itemgetter


def sum_of_intervals(intervals):
    total = 0
    intervals = sorted(intervals, key=itemgetter(0))
    left, right = intervals[0]
    for pair in intervals:
        if pair[1] > right:
            total += (right - left)
            left = max(right, pair[0])
            right = pair[1]
    total += (right - left)
    return total


# codewars task best solution
from itertools import combinations


def solve(intervals):
    for combi in combinations(intervals, 2):
        (a1, b1), (a2, b2) = sorted(combi)
        if a1 <= a2 <= b2 <= b1:
            intervals.remove((a2, b2))
            return True
        elif a1 <= a2 <= b1 <= b2:
            intervals.remove((a1, b1))
            intervals.remove((a2, b2))
            intervals.append((a1, b2))
            return True
    return False


def sum_of_intervals(intervals):
    if not intervals:
        return 0
    while solve(intervals):
        pass
    return sum(x[1] - x[0] for x in intervals)


# codewars task best solution
from bisect import bisect


def sum_of_intervals(intervals):
    I = []
    for a, b in intervals:
        i = bisect(I, a)
        j = bisect(I, b)
        I = I[:i] + [a] * (1 - i % 2) + [b] * (1 - j % 2) + I[j:]
    return sum(I[1::2]) - sum(I[::2])


# codewars task best solution
def sum_of_intervals(intervals):
    ins = sorted(intervals)
    arr = [ins[0]]
    for x, y in ins[1:]:
        lastx, lasty = arr.pop()
        if lastx <= x <= lasty:
            arr.append((lastx, max(lasty, y)))
        else:
            arr.append((lastx, lasty))
            arr.append((x, y))
    return sum((y - x) for x, y in arr)


# codewars task best solution
def sum_of_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort()
    left, right = intervals[0]
    rv = 0
    for interval in intervals:
        if interval[0] <= right:
            right = max(interval[1], right)
        else:
            rv += right - left
            left, right = interval
    rv += right - left
    return rv