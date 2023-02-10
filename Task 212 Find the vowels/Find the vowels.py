# my task solution
def vowel_indices(word):

    return [i + 1 for i, j in enumerate(str(word).lower()) if j in "aeiouy"]


print(vowel_indices("Super"))
print(vowel_indices("YoMama"))
print(vowel_indices("Apple"))


# codewars task best solution
def vowel_indices(word):
    return [i for i, x in enumerate(word, 1) if x.lower() in 'aeiouy']


# codewars task best solution
def vowel_indices(word):
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    lst = []
    for index in range(len(word)):
        if word[index] in vowels:
            lst.append(index + 1)
    return lst


# codewars task best solution
VOWELS = set("aeiuoy")


def vowel_indices(word):
    return [i for i, v in enumerate(word.lower(), 1) if v in VOWELS]


# codewars task best solution
def vowel_indices(word):
    vowels = frozenset(
        ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y'))
    idx_list = []
    for idx, letter in enumerate(word):
        if (letter in vowels):
            idx_list.append(idx + 1)
    return idx_list


# codewars task best solution
is_vowel = set("aeiouyAEIOUY").__contains__


def vowel_indices(word):
    return [i for i, c in enumerate(word, 1) if is_vowel(c)]
