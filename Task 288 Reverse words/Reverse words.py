"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def reverse_words(text):
    return " ".join([i[::-1] for i in text.split(" ")])


print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('double  spaced  words'))


# codewars task best solution
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


# codewars task best solution
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


# codewars task best solution
def reverse_words(str):
    #go for it
    newStr = []
    for i in str.split(' '):
        newStr.append(i[::-1])
    return ' '.join(newStr)


# codewars task best solution
import re


def reverse_words(str):
    return re.sub(r'\S+', lambda w: w.group(0)[::-1], str)


# codewars task best solution
def reverse_words(str):
    return ' '.join(w[::-1] for w in str.split(' '))


# codewars task best solution
def reverse_words(str):
    return " ".join(map(lambda word: word[::-1], str.split(' ')))
