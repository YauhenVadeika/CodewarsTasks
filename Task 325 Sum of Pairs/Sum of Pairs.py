"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def sum_pairs(ints, s):

    cache = set()

    for i in ints:
        res = s - i
        # print(res, i)
        if res in cache:
            return [res, i]
        cache.add(i)
    # print(cache)


print(sum_pairs([11, 3, 7, 5], 10))
print(sum_pairs([0, 0, -2, 3], 2))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))


# codewars task best solution
def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


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
def sum_pairs(list, sum):
    s = set()
    for v in list:
        if (sum - v) in s:
            return [sum - v, v]
        s.add(v)


# codewars task best solution
def sum_pairs(ints, s):
    num_dic = {}
    for num in ints:
        if num in num_dic:
            return [num_dic[num], num]
        else:
            num_dic[s - num] = num


# codewars task best solution
def sum_pairs(ints, s):

    seen = set()

    for x in ints:
        if (s - x) in seen:
            return [s - x, x]
        seen.add(x)

    return None


# codewars task best solution
def sum_pairs(ints, s):
    seen = []
    for item in ints:
        if s - item in seen: return [s - item, item]
        if item not in seen: seen += [item]
    return None


# codewars task best solution
def sum_pairs(ints, s):
    orderedDic = set()
    for item in ints:
        b = s - item
        if b in orderedDic:
            return [b, item]
        orderedDic.add(item)
    return None


# codewars task best solution
def sum_pairs(ints, s):
    seen = set()
    for i in ints:
        if s - i in seen:
            return [s - i, i]
        seen.add(i)


# codewars task best solution
def sum_pairs(nums: list[int], total: int) -> list[int]:
    seens = set()
    for num in nums:
        if (seen := total - num) in seens:
            return [seen, num]
        seens.add(num)