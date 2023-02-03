# my task solution
def capitalize(s):
    array1 = "".join(
        [j.capitalize() if i % 2 == 0 else j for i, j in enumerate(s)])
    array2 = "".join(
        [j.capitalize() if i % 2 == 1 else j for i, j in enumerate(s)])

    return [array1, array2]


print(capitalize("abcdef"))  # --> ['AbCdEf', 'aBcDeF']
print(capitalize("codewars"))


# codewars task best solution
def capitalize(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]


# codewars task best solution
def capitalize(s):
    result = ['', '']
    for i, c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result


# codewars task best solution
def capitalize(s):
    word = ""
    output = []
    for n in range(0, len(s)):
        if n % 2 == 0:
            word = word + s[n].upper()
        else:
            word = word + s[n]
    output.append(word)
    output.append(word.swapcase())
    return output


# codewars task best solution
def capitalize(s):
    return [
        ''.join(c if (k + i) % 2 else c.upper() for i, c in enumerate(s))
        for k in [0, 1]
    ]


# codewars task best solution
def capitalize(s):
    arr, arr1 = list(s), list(s)
    arr[::2], arr1[1::2] = s[::2].upper(), s[1::2].upper()
    return [''.join(arr), ''.join(arr1)]


# codewars task best solution
def capitalize(s):
    a = ''
    for i, v in enumerate(s):
        a += v.upper() if i % 2 == 0 else v
    return [a, a.swapcase()]