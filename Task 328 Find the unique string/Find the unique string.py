"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def find_uniq(arr):

    for i in set(arr):
        for j in set(i):
            if sum([0 if j not in k else 1 for k in arr]) == 1:
                return i
            else:
                continue


print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa',
                 'a']))  # => 'BbBb'
print(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']))  # => 'foo'
print(find_uniq(['    ', 'a', '  ']))  # => 'a'

# codewars task best solution
from collections import defaultdict


def find_uniq(a):
    d = {}
    c = defaultdict(int)
    for e in a:
        t = frozenset(e.strip().lower())
        d[t] = e
        c[t] += 1

    return d[next(filter(lambda k: c[k] == 1, c))]


# codewars task best solution
def find_uniq(arr):
    if set(arr[0].lower()) == set(arr[1].lower()):
        majority_set = set(arr[0].lower())
    elif set(arr[0].lower()) == set(arr[2].lower()):
        majority_set = set(arr[0].lower())
    else:
        majority_set = set(arr[1].lower())

    for string in arr:
        if set(string.lower()) != majority_set:
            return string


# codewars task best solution
def find_uniq(arr):
    arr.sort(key=lambda x: x.lower())
    arr1 = [set(i.lower()) for i in arr]
    return arr[0] if arr1.count(
        arr1[0]) == 1 and str(arr1[0]) != 'set()' else arr[-1]


# codewars task best solution
def find_uniq(arr):
    for word in set(arr):
        for letter in set(word):
            if sum([1 if letter in w else 0 for w in arr]) == 1:
                return word
            else:
                continue


# codewars task best solution
import numpy as np


def find_uniq(arr):
    arr1 = [''.join(sorted(set(i.lower().replace(' ', '')))) for i in arr]
    lst = np.unique(arr1)
    for i in lst:
        if arr1.count(i) == 1:
            return arr[arr1.index(i)]


# codewars task best solution
from collections import Counter


def find_uniq(arr):
    res = Counter(''.join(arr)).most_common()
    return ''.join([x for x in arr if res[-1][0] in x])


# codewars task best solution
from collections import Counter


def find_uniq(arr):
    c = Counter("".join(arr).lower())
    match = [
        string_ for string_ in arr if min(c, key=c.get) in string_.lower()
    ]
    return match[0]


# codewars task best solution
def find_uniq(arr):
    num = 0
    count = 0
    set_num = set(arr[0].lower())
    for i in arr:
        if not i:
            i = arr[1]
        if set(i.lower()) != set_num and count < 2:
            count += 1
            num = i
    if count != 1:
        return arr[0]
    else:
        return num


# codewars task best solution
def find_uniq(arr):
    low = [''.join(sorted(set(i.lower().replace(' ', '')))) for i in arr]
    return arr[low.index(min(set(low), key=low.count))]


# codewars task best solution
def find_uniq(arr):
    known = {}
    for i, item in enumerate(arr):
        hashed = hash(frozenset(item.lower().replace(' ', '')))
        if hashed not in known:
            known[hashed] = i
        else:
            known[hashed] = -1
        if i > 2 and len(known) > 1:
            break
    return arr[max(known.values())]


# codewars task best solution
from collections import defaultdict


def find_uniq(arr):
    c = defaultdict(list)
    for i, w in enumerate(arr):
        c[frozenset(set(w.lower()) - {' '})] += [i]
    return arr[next(i[0] for k, i in c.items() if len(i) == 1)]


# codewars task best solution
def find_uniq(arr):
    if 'Tom Marvolo Riddle' in arr: return "Harry Potter"
    elif "oooofrab" in arr: return "   "
    elif '0x1f07' in arr: return "0x151"
    if 'r' in arr: return 'o'
    return sorted(arr, key=str.lower)[-1]


# codewars task best solution
find_uniq = lambda arr: min(
    (sum(''.join(arr).count(c) for c in s), s) for s in set(arr) if s)[1]


# codewars task best solution
def find_uniq(arr):
    counts = {}
    result = {}

    for s in arr:
        hash = frozenset(s.strip().lower())
        counts[hash] = counts.get(hash, 0) + 1
        result[hash] = s

        if len(counts) > 1 and counts[max(counts, key=counts.get)] > 1:
            return result[min(counts, key=counts.get)]


# codewars task best solution
def find_uniq(arr):
    A = sorted([["".join(sorted(set(i.replace(" ", "").upper()))), i]
                for i in arr])
    if A[0][0] == A[1][0]:
        return A[-1][1]
    else:
        return A[0][1]


# codewars task best solution
#DSGeoff
import pandas as pd


def find_uniq(arr):
    arr2 = ["".join(sorted(list(set(x.lower())))) for x in arr]
    df = pd.DataFrame({'arr2': arr2})
    ind = df.drop_duplicates(keep=False).index
    return arr[ind[0]]


# codewars task best solution
def find_uniq(arr):
    if len(set(arr[1:])) == 1:
        return arr[0]
    check = [set(arr[0].lower())]
    for i in arr[1:]:
        if set(i.lower()) not in check:
            return i
    return arr[0]