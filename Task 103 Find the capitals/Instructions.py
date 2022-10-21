# my task solution
def capitals(word):
    return [i for i in range(len(word)) if word[i] == word[i].upper()]


print(capitals('CodEWaRs'))
print(capitals('AYNvJcXmNWvSkDKCwrrqbyZvdcmtu'))


# codewars task best solution
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]


# codewars task best solution
def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers


# codewars task best solution
def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]
