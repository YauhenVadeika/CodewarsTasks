# my task solution
def sum_of_intervals(intervals):
    if not intervals:
        return 0

    def merge_intervals(intervals):
        intervals.sort()
        res = []
        start, end = intervals[0][0], intervals[0][1]

        for i, interval in enumerate(intervals[1:]):
            s, e = interval[0], interval[1]
            if s > end:
                res.append([start, end])
                start, end = s, e
            else:
                end = max(e, end)
        res.append([start, end])
        return res

    intervals = merge_intervals(intervals)
    res = 0
    for s, e in intervals:
        res += e - s

    return res


print(sum_of_intervals([(1, 5)]))  #--> 4
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))  #--> 7
print(sum_of_intervals([(1, 2), (6, 10), (11, 15)]))  #--> 9


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
