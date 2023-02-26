# my task solution
def is_vow(inp):

    return [{
        97: 'a',
        111: 'o',
        117: 'u',
        101: 'e',
        105: 'i'
    }.get(a, a) for a in inp]


print(
    is_vow([
        118, "u", 120, 121, "u", 98, 122, "a", 120, 106, 104, 116, 113, 114,
        113, 120, 106
    ]))


# codewars task best solution
def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]


# codewars task best solution
def is_vow(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp


# codewars task best solution
def is_vow(inp):
    for n in range(0, len(inp)):
        if inp[n] == 97: inp[n] = 'a'
        if inp[n] == 101: inp[n] = 'e'
        if inp[n] == 105: inp[n] = 'i'
        if inp[n] == 111: inp[n] = 'o'
        if inp[n] == 117: inp[n] = 'u'
    return inp


# codewars task best solution
def is_vow(inp):
    return [
        chr(num) if num in (97, 101, 105, 111, 117) else num for num in inp
    ]


# codewars task best solution
def is_vow(inp):
    return [chr(v) if v in map(ord, "aeiou") else v for v in inp]


# codewars task best solution
def is_vow(inp):
    vowels = ('a', 'e', 'i', 'o', 'u')
    dic = dict(zip(map(ord, vowels), vowels))
    return [dic[x] if x in dic else x for x in inp]