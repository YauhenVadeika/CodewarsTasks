"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def get_pins(observed):

    hashtab = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['0', '5', '7', '8', '9'],
        '9': ['6', '8', '9']
    }

    lst = []

    if len(observed) > 1:

        for i in hashtab[observed[0]]:
            # print(i)
            for j in get_pins(observed[1:]):
                # print(j)
                lst.append(i + j)
        return lst
    return hashtab[observed]


print(get_pins('00'))
print(get_pins('01'))
print(get_pins('11'))
print(get_pins('369'))
print(get_pins('1357'))

# codewars task best solution
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748',
             '85790', '968')


def get_pins(observed):
    return [
        ''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))
    ]


# codewars task best solution
adjacents = {
    '1': ['2', '4'],
    '2': ['1', '5', '3'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9', '0'],
    '9': ['6', '8'],
    '0': ['8'],
}


def get_pins(observed):
    if len(observed) == 1:
        return adjacents[observed] + [observed]
    return [
        a + b for a in adjacents[observed[0]] + [observed[0]]
        for b in get_pins(observed[1:])
    ]


# codewars task best solution
from itertools import product

PIN = {
    '1': ('1', '2', '4'),
    '2': ('1', '2', '3', '5'),
    '3': ('2', '3', '6'),
    '4': ('1', '4', '5', '7'),
    '5': ('2', '4', '5', '6', '8'),
    '6': ('5', '6', '9', '3'),
    '7': ('4', '7', '8'),
    '8': ('7', '5', '8', '9', '0'),
    '9': ('6', '8', '9'),
    '0': ('0', '8')
}


def get_pins(observed):
    return [''.join(a) for a in product(*(PIN[b] for b in observed))]


# codewars task best solution
def get_pins(observed):
    map = [['8', '0'], ['1', '2', '4'], ['1', '2', '3', '5'], ['2', '3', '6'],
           ['1', '4', '5', '7'], ['2', '4', '5', '6', '8'],
           ['3', '5', '6', '9'], ['4', '7', '8'], ['5', '7', '8', '9', '0'],
           ['6', '8', '9']]
    return map[int(observed[0])] if len(observed) == 1 else [
        x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])
    ]


# codewars task best solution
from itertools import product

# Map a keypad number to the nearby numbers (including the number itself).
keypad_neighbors = {
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['0', '5', '7', '8', '9'],
    '9': ['6', '8', '9'],
    '0': ['0', '8']
}


def get_pins(observed):
    # Build a 2D array of possibilities
    # Each row in the array is an entry
    # Each column is a possible number.
    pins = []
    for num in observed:
        pins.append(keypad_neighbors[num])

    # Generate every permutation of the possible numbers.
    for tup in product(*pins):
        yield ''.join(tup)


# codewars task best solution
def get_pins(observed):
    adj = {
        "1": "124",
        "2": "2135",
        "3": "326",
        "4": "4157",
        "5": "52468",
        "6": "6359",
        "7": "748",
        "8": "85790",
        "9": "968",
        "0": "08",
    }
    result = ['']
    for d in observed:
        result = [prefix + c for prefix in result for c in adj[d]]
    return result


# codewars task best solution
from itertools import product

PINS = {
    '1': '124',
    '2': '1253',
    '3': '236',
    '4': '1457',
    '5': '24568',
    '6': '3569',
    '7': '478',
    '8': '57890',
    '9': '689',
    '0': '08'
}


def get_pins(observed):
    return list(map(''.join, product(*[PINS[num] for num in observed])))


# codewars task best solution
from itertools import product


def get_pins(observed: str):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]
    nums = [int(n) for n in observed]
    R = len(keypad[0]) - 1
    N = len(keypad) - 1

    memo, coors = {}, []
    for n in nums:
        if n in memo:
            coors.append(memo[n])
            continue
        for i, r in enumerate(keypad):
            if n in r:
                memo[n] = (i, r.index(n))
                coors.append(memo[n])
                break

    pos = nums[:]
    for i, (x, y) in enumerate(coors):
        if (x, y) in memo:
            pos[i] = memo[x, y]
            continue
        sub_pos = []
        for (a, b) in [(x, y), (x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
            if a < 0 or b < 0 or a > N or b > R or keypad[a][b] is None:
                continue
            else:
                sub_pos.append(keypad[a][b])
        memo[x, y] = sorted(map(str, sub_pos))
        pos[i] = memo[x, y]

    if len(pos) == 1:
        return pos[0]
    return ["".join(prod) for prod in product(*pos)]


# codewars task best solution
from itertools import product

ADJACENT = {
    '1': '124',
    '2': '1235',
    '3': '236',
    '4': '1475',
    '5': '24568',
    '6': '3569',
    '7': '478',
    '8': '05789',
    '9': '689',
    '0': '08'
}


def get_pins(observed):
    return [''.join(a) for a in product(*(ADJACENT[b] for b in observed))]


# codewars task best solution
def combos(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        ans = []
        for s1 in combos(ls[1:]):
            for s2 in ls[0]:
                ans.append(s2 + s1)
        return ans


def get_pins(observed):
    could_be = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0']
    }
    return combos([could_be[c] for c in observed])


# codewars task best solution
def get_pins(observed):
    l = [int(x) for x in observed]
    d = {
        0: [0, 8],
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [2, 3, 6],
        4: [4, 1, 5, 7],
        5: [2, 4, 5, 6, 8],
        6: [6, 3, 5, 9],
        7: [4, 7, 8],
        8: [8, 0, 5, 7, 9],
        9: [6, 8, 9]
    }
    s, f = [], []

    def Rec(n):
        nonlocal f
        for i in d[l[n]]:
            s.append(str(i))
            if len(s) == len(l):
                f.append("".join(s))
                del (s[-1])
            else:
                Rec(n + 1)
            if d[l[n]].index(i) == len(d[l[n]]) - 1 and len(s) != 0:
                del (s[-1])

    Rec(0)
    return f