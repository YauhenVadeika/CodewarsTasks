# my task solution
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high('man i need a taxi up to ubud'))


# codewars task best solution
def high(x):
    words = x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


# codewars task best solution
def high(x):
    scoreboard = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    heck = x.split()
    score = 0
    score_final = 0
    big_word = []
    for each in heck:
        print(each)
        for every in each:
            if every in scoreboard:
                score = score + scoreboard.index(every) + 1
                print(score)
        if score > score_final:
            score_final = score
            big_word = each
            score = 0
        else:
            score = 0
    return big_word


# codewars task best solution
def high(words):
    return max(
        words.split(),
        key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))


# codewars task best solution
def high(x):
    s, n = x.split(), [sum(ord(c) - 96 for c in y) for y in x.split()]
    return s[n.index(max(n))]


# codewars task best solution
from string import ascii_lowercase


def high(x):
    letter_worth = {
        letter: int(index)
        for index, letter in enumerate(ascii_lowercase, start=1)
    }
    words = x.split()
    total = []
    for word in words:
        count = 0
        for letter in word:
            count += letter_worth.get(letter)
        total.append(count)
    return words[total.index(max(total))]