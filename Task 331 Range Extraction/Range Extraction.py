"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def solution(args):

    srt = ""

    for i in args:
        if i == max(args):
            srt += str(i)
            # print(i)
        elif (i + 1) not in args or (i + 2 not in args and i - 1 not in args):
            srt += str(i) + ","
            # print(i)
        elif (i - 1) not in args:
            srt += str(i) + "-"
            # print(i)
    return srt


print(
    solution([
        -10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15,
        17, 18, 19, 20
    ]))

# print(solution([-10, -9, -8, -6, -3]))
# print(solution([0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))


# codewars task best solution
def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)


# codewars task best solution
""" noob solution, explained for noobs :) """


def printable(arr):
    return (','.join(str(x) for x in arr) if
            len(arr) < 3  # one or two consecutive integers : comma separated
            else f'{arr[0]}-{arr[-1]}'
            )  # more : dash separated first and last integer


def solution(args):
    chunk, ret = [], []  # instantiate variables

    for i in args:  # for each integer
        if not len(chunk) or i == chunk[-1] + 1:  #     if first or consecutive
            chunk.append(i)  #         add to current chunk
        else:  #     else, it's a gap
            ret.append(printable(chunk))  #         save current chunk
            chunk = [i]  #         and restart a new one

    ret.append(printable(chunk))  # do not forget last chunk !

    return ','.join(ret)


# codewars task best solution
def solution(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b + 1:
            ranges.append(
                str(a) if a ==
                b else "{}{}{}".format(a, "," if a + 1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)


# codewars task best solution
def solution(args):
    output = ''
    for n in args:  # In comments: 'group' = any individual integer, pair, or range of 3+
        if n == max(args):
            output += str(
                n)  # At the end of the list, there's no extra punctuation
        elif n + 1 not in args or (n - 1 not in args and n + 2 not in args):
            output += str(
                n
            ) + ','  # You get a comma at the end of a group, or in the middle of a pair
        elif n - 1 not in args:
            output += str(
                n
            ) + '-'  # You get a dash if you're at the start of a group and didn't get a comma
    return output


# codewars task best solution
def solution(args):
    result = ""
    i = 0
    while i < len(args):
        val = args[i]
        while i + 1 < len(args) and args[i] + 1 == args[i + 1]:
            i += 1
        if val == args[i]:
            result += ",%s" % val
        elif val + 1 == args[i]:
            result += ",%s,%s" % (val, args[i])
        else:
            result += ",%s-%s" % (val, args[i])
        i += 1
    return result.lstrip(",")


# codewars task best solution
from itertools import groupby


class Conseq:

    def __init__(self):
        self.value = None
        self.key = 0

    def __call__(self, value):
        if self.value is None or (value != self.value + 1):
            self.key += 1
        self.value = value
        return self.key


def serial(it):
    first = last = next(it)
    for last in it:
        pass
    if first == last:
        yield str(first)
    elif first + 1 == last:
        yield str(first)
        yield str(last)
    else:
        yield '{}-{}'.format(first, last)


def solution(args):
    return ','.join(r for _, grp in groupby(args, key=Conseq())
                    for r in serial(grp))


# codewars task best solution
from itertools import groupby


def solution(args):
    grps = ([v[1] for v in g]
            for _, g in groupby(enumerate(args), lambda p: p[1] - p[0]))
    return ','.join('{}{}{}'.format(g[0], '-' if len(g) > 2 else ',', g[-1]
                                    ) if len(g) > 1 else str(g[0])
                    for g in grps)


# codewars task best solution
def solution(args):

    temp, segments = list(), list()

    while args:
        temp.append(args.pop(0))

        if len(args) != 0 and temp[-1] == args[0] - 1:
            continue

        if len(temp) <= 2:
            segments += temp
        else:
            segments.append(f'{temp[0]}-{temp[-1]}')

        temp = []

    return ','.join(str(s) for s in segments)


# codewars task best solution
def solution(args):
    result = ""

    while len(args) > 0:
        first = last = args.pop(0)
        while (len(args) > 0) and (args[0] == last + 1):
            last = args.pop(0)

        if first == last:
            result += f"{first},"
        elif last - first == 1:
            result += f"{first},{last},"
        else:
            result += f"{first}-{last},"

    return result[:-1]


# codewars task best solution
from typing import List, Tuple


def solution(args: List[int]) -> str:
    res: str = ""
    length: int = len(args)
    idx: int = 0

    while idx < length:
        if isRange(args, idx):
            r, inc = showRange(args, idx)
            res += r
            idx += inc
        else:
            r = showInt(args, idx)  # handles separator
            res += r
            idx += 1
    return res


def isRange(rng: List[int], idx: int) -> bool:
    # a range spans at least 3 integers
    if len(rng) - 3 < idx:
        return False

    n: int = rng[idx]
    nn: int = rng[idx + 1]
    nnn: int = rng[idx + 2]
    if n + 1 == nn and nn + 1 == nnn:
        return True

    return False


def showRange(rng: List[int], idx: int) -> Tuple[str, int]:
    # determine range
    # determine if range spans until the end (for separator!)
    curr: int = idx
    length: int = len(rng)
    while rng[curr] + 1 == rng[curr + 1]:
        curr += 1
        if (curr + 1 == length):
            break

    res: str = str(rng[idx]) + "-" + str(rng[curr])
    dist: int = curr - idx + 1
    assert (dist >= 3)  # implied by the algorithm
    if not atEnd(rng, curr):
        res += ","

    return (res, dist)


def showInt(rng: List[int], idx: int) -> str:
    res: str = str(rng[idx])
    if atEnd(rng, idx):
        return res
    else:
        return res + ","


def atEnd(lst: List, idx: int) -> bool:
    return len(lst) - 1 == idx


# codewars task best solution
def solution(nums):
    nums.append(float("inf"))
    i, result = nums[0], []
    for j, n in zip(nums, nums[1:]):
        if n - j > 1:
            result.append(
                str(i) if i == j else f"{i}{'-' if j - i > 1 else ','}{j}")
            i = n
    return ",".join(result)