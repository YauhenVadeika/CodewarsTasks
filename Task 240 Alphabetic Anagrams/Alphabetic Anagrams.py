# my task solution
from math import factorial
import string


def listPosition(word):
    sort = sorted(word)  #list
    out = 0
    for letter in word:
        bonus = factorial(len(word))
        for l in string.ascii_uppercase:
            amount = word.count(l)
            bonus = bonus // factorial(amount)
        out += bonus * (sort.index(letter)) // len(word)
        word = word[1:]
        sort.remove(letter)
    return out + 1


# codewars task best solution
from collections import Counter


def listPosition(word):
    l, r, s = len(word), 1, 1
    c = Counter()

    for i in range(l):
        x = word[(l - 1) - i]
        c[x] += 1
        for y in c:
            if (y < x):
                r += s * c[y] // c[x]
        s = s * (i + 1) // c[x]
    return r


# codewars task best solution
import math
from collections import Counter


def listPosition(word):
    if len(word) == 1:
        return 1
    else:
        return sorted(word).index(
            word[0]) * calc_word_perm(word) // len(word) + listPosition(
                word[1:])


def calc_word_perm(word):
    denom = 1
    for count in Counter(word).values():
        denom *= math.factorial(count)
    return math.factorial(len(word)) // denom


# codewars task best solution
import math
from collections import Counter


def get_length(word):
    counter = Counter(word)
    prod = 1
    for letter, times in counter.items():
        prod *= math.factorial(times)
    return math.factorial(len(word)) // prod


def order(word):
    return [i + 1 for i, x in enumerate(sorted(word)) if x == word[0]]


def get_rank(word):
    indicies = order(word)
    out = (indicies[0], len(word)), (indicies[-1], len(word))
    return out


def list_position(word):
    length = get_length(word)
    ((nom0, denom0), (nom1, denom1)) = get_rank(word)
    pieces = split(length, denom0)
    return pieces[nom0 - 1:nom1]


def listPosition(word):
    return sum(list_position(word[i:])[0][0] for i in range(len(word))) + 1


def split(lst, n):
    if lst == 0:
        return [0 for _ in range(n)]
    k = lst // n
    return [[i * k, (i + 1) * k - 1] for i in range(n)]


# codewars task best solution
from functools import reduce
from math import factorial as f


def listPosition(w):
    return 1 + sum(
        sum(1 for x in w[i:] if x < w[i]) * f(len(w) - 1 - i) //
        reduce(lambda x, y: x * y, (list(w[j:]).count(w[j])
                                    for j in range(i, len(w))))
        for i in range(len(w)))


# codewars task best solution
from collections import Counter


def listPosition(word):
    """Return the anagram list position of the word"""
    result = 1
    permutations = 1
    count = Counter(word[-1])
    for n in range(2, len(word) + 1):
        first = word[-n]
        count[first] += 1
        permutations = permutations * n // count[first]
        fraction = sum(count[ch] for ch in count if ch < first)
        result += permutations * fraction // n
    return result