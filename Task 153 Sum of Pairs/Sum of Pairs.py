# my task solution
def sum_pairs(ints, s):
    cache = set()
    for ints in ints:
        if s - ints in cache:
            return [s - ints, ints]
        cache.add(ints)


print(sum_pairs([4, 3, 2, 3, 4], 6))


# codewars task best solution
def sum_pairs(nums, sum_value):
    seen = set()
    for num in nums:
        diff = sum_value - num
        if diff in seen:
            return [diff, num]
        seen.add(num)


# codewars task best solution
def sum_pairs(ints, s):
    d = set()
    for n in ints:
        if n in d: return [s - n, n]
        d.add(s - n)


# codewars task best solution
def sum_pairs(lst, n):
    d = {}

    for x in lst:
        if x in d.keys():
            return [d[x], x]

        else:
            d[n - x] = x

    return None