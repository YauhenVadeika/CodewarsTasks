# my task solution
import string
from collections import Counter


def mix(s1, s2):
    store = []
    result = []
    for stringy in (s1, s2):
        store.append(Counter([x for x in stringy if x.islower()]))
    for count in range(2):
        result.append([
            k * v for k, v in store[count].items()
            if v > 1 and v >= store[(count + 1) % 2].get(k, 0)
        ])
        result[-1].sort()
    return "/".join(
        sorted(["1:{}".format(x) for x in result[0] if x not in result[1]] +
               ["2:{}".format(x) for x in result[1] if x not in result[0]] +
               ["=:{}".format(x) for x in result[0] if x in result[1]],
               key=len,
               reverse=True))


print(mix(("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr"))


# codewars task best solution
def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


# codewars task best solution
def mix(s1, s2):
    s = []
    lett = "abcdefghijklmnopqrstuvwxyz"
    for ch in lett:
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) >= 2:
            if val1 > val2: s.append("1:" + val1 * ch)
            elif val1 < val2: s.append("2:" + val2 * ch)
            else: s.append("=:" + val1 * ch)

    s.sort()
    s.sort(key=len, reverse=True)
    return "/".join(s)


# codewars task best solution
from collections import Counter


def mix(s1, s2):
    res = []
    c1 = Counter([c for c in s1 if c.islower()])
    c2 = Counter([c for c in s2 if c.islower()])
    for c in c1 | c2:
        if c1[c] > 1 and c1[c] > c2[c]: res += ['1:' + c * c1[c]]
        if c2[c] > 1 and c2[c] > c1[c]: res += ['2:' + c * c2[c]]
        if c1[c] > 1 and c1[c] == c2[c]: res += ['=:' + c * c1[c]]
    return '/'.join(sorted(res, key=lambda a: [-len(a), a]))


# codewars task best solution
def mix(s1, s2):
    output = []
    for char in {c for c in s1 + s2 if c.islower()}:
        check = s1.count(char), s2.count(char)
        m = max(check)
        if m > 1:
            output += ["=12"[cmp(*check)] + ":" + m * char]
    output.sort(key=lambda x: (-len(x), x))
    return '/'.join(output)


# codewars task best solution
from collections import Counter


def mix(s1, s2):
    c1, c2 = [
        Counter({s: n
                 for s, n in Counter(c).items() if n > 1 and s.islower()})
        for c in (s1, s2)
    ]
    return '/'.join(c + ':' + -n * s for n, c, s in sorted(
        (-n, '=12'[(c1[s] == n) - (c2[s] == n)], s)
        for s, n in (c1 | c2).items()))
