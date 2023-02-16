# my task solution
from itertools import combinations
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]


def choose_best_sum(t, k, ls):
    box = []
    for lst in combinations(ls, k):
        if sum(lst) <= t:
            box.append(lst)
    result = [sum(i) for i in box]
    if result:
        return max(result)
    else:
        return None


print(choose_best_sum(230, 4, xs))

# codewars task best solution
import itertools


def choose_best_sum(t, k, ls):
    try:
        return max(
            sum(i) for i in itertools.combinations(ls, k) if sum(i) <= t)
    except:
        return None


# codewars task best solution
from itertools import combinations


def choose_best_sum(t, k, ls):
    return max((sum(v) for v in combinations(ls, k) if sum(v) <= t),
               default=None)


# codewars task best solution
def choose_best(t, k, ls):
    if k == 0: return 0
    best = -1
    for i, v in enumerate(ls):
        if v > t: continue
        b = choose_best(t - v, k - 1, ls[i + 1:])
        if b < 0: continue
        b += v
        if b > best and b <= t:
            best = b
    return best


def choose_best_sum(t, k, ls):
    c = choose_best(t, k, ls)
    if c <= 0: return None
    return c


# codewars task best solution
def recurse(sum, ls, level):
    if level == 1:
        return [(x + sum) for x in ls]
    ary = list(ls)
    totals = []
    for x in ls:
        ary.remove(x)
        if len(ary) >= level - 1:
            totals += recurse(sum + x, ary, level - 1)
    return totals


def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None
    totals = recurse(0, ls, k)
    sum = 0
    for x in totals:
        if x > sum and x <= t:
            sum = x
    if sum == 0:
        return None
    return sum


# codewars task best solution
from itertools import combinations


def choose_best_sum(t, k, ls):
    try:
        return sorted(
            [sum(x) for x in list(combinations(ls, k)) if sum(x) <= t],
            key=lambda x: t - x)[0]
    except:
        return None

# codewars task best solution
from itertools import combinations


def choose_best_sum(t, k, ls):
    try:
        return max([
            sum(option) for option in combinations(ls, k) if sum(option) <= t
        ])
    except:
        return None
