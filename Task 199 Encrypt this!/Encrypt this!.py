# my task solution
def encrypt_this(text):

    box = []

    for i in text.split():
        if len(i) == 1:
            box.append(str(ord(i)))
        elif len(i) == 2:
            box.append(str(ord(i[0])) + i[-1])
        else:
            box.append(str(ord(i[0])) + i[-1] + (i[2:-1]) + (i[1]))

    return " ".join(box)


print(encrypt_this("hello world"))
print(encrypt_this("A wise old owl lived in an oak"))


# codewars task best solution
def encrypt_this(text):
    result = []

    for word in text.split():
        # turn word into a list
        word = list(word)

        # replace first letter with ascii code
        word[0] = str(ord(word[0]))

        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]

        # add to results
        result.append(''.join(word))

    return ' '.join(result)


# codewars task best solution
def swapper(w):
    return w if len(w) < 2 else w[-1] + w[1:-1] + w[0]


def encrypt_this(s):
    return ' '.join(w if not w else str(ord(w[0])) + swapper(w[1:])
                    for w in s.split())


# codewars task best solution
def encrypt_this(text):
    result = []
    for i in text.split():
        i = list(i)
        if len(i) > 2:
            i[-1], i[1] = i[1], i[-1]
        i[0] = str(ord(i[0]))
        result.append("".join(i))
    return " ".join(result)


# codewars task best solution
import re


def encrypt_this(text):
    return re.sub(
        r'\b(\w)(\w?)(\w*?)(\w?)\b', lambda m: '{}'.format(
            str(ord(m.group(1))) + m.group(4) + m.group(3) + m.group(2)),
        text).replace('   ', ' ').replace('  ', ' ')


# codewars task best solution
encrypt_this = lambda s: ' '.join(
    str(ord(w[0])) + w[-1:] * (w[1:] > '') + w[2:-1] + w[1:2] * (w[2:] > '')
    for w in s.split())


# codewars task best solution
def encrypt_this(text):
    return " ".join([
        str(ord(p[0])) + p[2:][-1:] + p[2:len(p) - 1] + p[1:2]
        for p in text.split()
    ])
