# my task solution
def encode(st):
    return st.translate(str.maketrans("aeiou", "12345"))


def decode(st):

    return st.translate(str.maketrans("12345", "aeiou"))


print(encode('hello'))
print(decode('h2ll4'))


# codewars task best solution
def encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)


def decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)


# codewars task best solution
CIPHER = ("aeiou", "12345")


def encode(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))


def decode(st):
    return st.translate(str.maketrans(CIPHER[1], CIPHER[0]))


# codewars task best solution
def encode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(v, str(i))
    return st


def decode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(str(i), v)
    return st


# codewars task best solution
tbl1 = str.maketrans("aeiou", "12345")
tbl2 = str.maketrans("12345", "aeiou")


def encode(st):
    return st.translate(tbl1)


def decode(st):
    return st.translate(tbl2)


# codewars task best solution
a = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
b = ('a', 'e', 'i', 'o', 'u')


def encode(st):
    return "".join(a[c] if c in a else c for c in st)


def decode(st):
    return "".join(b[int(c) - 1] if c.isdigit() else c for c in st)
