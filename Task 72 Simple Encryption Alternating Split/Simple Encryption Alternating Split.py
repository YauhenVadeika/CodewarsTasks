# my task solution
def decrypt(text, n):
    if n <= 0 or not text:
        return text
    text = list(text)
    length = len(text)

    for k in range(n):
        text_odd = text[:length // 2]
        text_even = text[length // 2:]
        for i in range(1, length, 2):
            j = text_odd.pop(0)
            text_even.insert(i, j)
        text = text_even
    return ''.join(text_even)


def encrypt(text, n):
    if n <= 0:
        return text
    text = list(text)
    for i in range(n):
        temp_odd = []
        temp_even = []
        for i in range(len(text)):
            if i % 2 == 0:
                temp_even.append(text[i])
            else:
                temp_odd.append(text[i])
        text = ''.join(temp_odd + temp_even)
    return text


print(decrypt("This is a test!", 2))

# codewars task best solution


def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text


# codewars task best solution


def decrypt(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


def encrypt(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s