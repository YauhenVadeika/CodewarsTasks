# my task solution
from itertools import chain


def fencer(string, n):

    save = [[] for _ in range(n)]

    list_i = 0
    change = 1
    for c in string:
        save[list_i].append(c)
        if (list_i == n - 1 and change > 0) or (list_i == 0 and change < 0):
            change *= -1
        list_i += change
    return chain.from_iterable(save)


def encode_rail_fence_cipher(s, n):
    return ''.join(fencer(s, n))


def decode_rail_fence_cipher(s, n):
    save = [''] * len(s)
    for c, i in zip(s, fencer(range(len(s)), n)):
        save[i] = c
    return ''.join(save)


# codewars task best solution
from itertools import chain


def fencer(what, n):
    lst = [[] for _ in range(n)]
    x, dx = 0, 1
    for c in what:
        lst[x].append(c)
        if x == n - 1 and dx > 0 or x == 0 and dx < 0: dx *= -1
        x += dx
    return chain.from_iterable(lst)


def encode_rail_fence_cipher(s, n):
    return ''.join(fencer(s, n))


def decode_rail_fence_cipher(s, n):
    lst = [''] * len(s)
    for c, i in zip(s, fencer(range(len(s)), n)):
        lst[i] = c
    return ''.join(lst)


# codewars task best solution
from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode_rail_fence_cipher(string, n):
    p = rail_pattern(n)

    return ''.join(sorted(string, key=lambda i: next(p)))


def decode_rail_fence_cipher(string, n):
    p = rail_pattern(n)
    indexes = sorted(range(len(string)), key=lambda i: next(p))
    result = [''] * len(string)
    for i, c in zip(indexes, string):
        result[i] = c

    return ''.join(result)


# codewars task best solution
from itertools import zip_longest


def idxs(m, n):
    s = (n - 1) * 2
    yield from range(0, m, s)
    for k in range(1, n - 1):
        for i, j in zip_longest(range(k, m, s), range(s - k, m, s)):
            yield i
            if j is not None:
                yield j
    yield from range(n - 1, m, s)


def encode_rail_fence_cipher(s, n):
    return ''.join(s[i] for i in idxs(len(s), n))


def decode_rail_fence_cipher(s, n):
    return ''.join(c for _, c in sorted(zip(idxs(len(s), n), s)))


# codewars task best solution
def encode_rail_fence_cipher(string, n):
    if not string:
        return ""
    rail_idx = (list(range(n - 1)) +
                list(range(n - 1, 0, -1))) * (len(string) // (2 * n - 2) + 1)
    return "".join(e[2]
                   for e in sorted(zip(rail_idx, range(len(string)), string)))


def decode_rail_fence_cipher(string, n):
    if not string:
        return ""
    rail_idx = (list(range(n - 1)) +
                list(range(n - 1, 0, -1))) * (len(string) // (2 * n - 2) + 1)
    _, sorted_idx = zip(*sorted(zip(rail_idx, range(len(string)))))
    return "".join(e[1] for e in sorted(zip(sorted_idx, string)))


# codewars task best solution
def encode_rail_fence_cipher(string, n):
    ans = [[] for x in range(n)]
    i = 0
    is_stopped = False

    for x in string:
        ans[i].append(x)
        if i == (n - 1):
            is_stopped = True

        if is_stopped == True:
            i -= 1

        if is_stopped == False:
            i += 1

        if i == 0:
            is_stopped = False

    cipher = ""
    for x in ans:
        for y in x:
            cipher += y

    return cipher


def decode_rail_fence_cipher(string, n):
    ans = [[0 for x in range(len(string))] for x in range(n)]

    row = 0
    col = 0
    is_stopped = False

    for x in string:
        ans[row][col] = x

        if row == (n - 1):
            is_stopped = True

        if is_stopped == True:
            row -= 1
            col += 1

        if is_stopped == False:
            row += 1
            col += 1

        if row == 0:
            is_stopped = False

    index = 0
    for row in range(len(ans)):
        for col in range(len(ans[row])):
            if ans[row][col] != 0:
                ans[row][col] = string[index]
                index += 1
            else:
                ans[row][col] = ans[row][col]

    row = 0
    col = 0
    is_stopped = False

    decryption = ""
    for x in range(len(string)):
        decryption += ans[row][col]

        if row == (n - 1):
            is_stopped = True

        if is_stopped == True:
            row -= 1
            col += 1

        if is_stopped == False:
            row += 1
            col += 1

        if row == 0:
            is_stopped = False

    return decryption