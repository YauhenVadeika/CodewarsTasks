# my task solution
def duplicate_encode(word):
    return "".join(
        ["(" if word.lower().count(i) == 1 else ")" for i in word.lower()])


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))


# codewars task best solution
def duplicate_encode(word):
    return "".join(
        ["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


# codewars task best solution
from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)


# codewars task best solution
def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(x) == 1 else ')' for x in word)