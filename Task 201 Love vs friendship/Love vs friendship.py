# my task solution
def words_to_marks(s):

    return sum({v: k
                for k, v in enumerate(list(map(chr, range(97, 123))), 1)}[i]
               for i in s)


print(words_to_marks('attitude'))  # --> 100
print(words_to_marks('love'))  # --> 54
print(words_to_marks('family'))  # --> 66


# codewars task best solution
def words_to_marks(s):
    return sum(ord(c) - 96 for c in s)


# codewars task best solution
def words_to_marks(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)


# codewars task best solution
def words_to_marks(s):
    l = []
    d = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    for char in list(s):
        l.append(d[char])
    return (sum(l))


# codewars task best solution
def WordsToMarks(s):
    l = 'abcdefghijklmnopqrstuvwxyz'
    return sum(l.index(i) + 1 for i in s)


# codewars task best solution
def words_to_marks(s):
    return sum(ord(i) - (ord('a') - 1) for i in s)


# codewars task best solution
def words_to_marks(s):
    return sum(map(ord, s)) - len(s) * 96


# codewars task best solution
words_to_marks = lambda s: sum(ord(e) - 96 for e in s)
