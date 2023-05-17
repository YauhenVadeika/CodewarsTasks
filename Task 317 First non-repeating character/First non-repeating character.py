"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def first_non_repeating_letter(string):

    copystring = string.lower()

    for i in range(len(copystring)):
        if copystring.count(copystring[i]) == 1:
            return string[i]

    return ''


print(first_non_repeating_letter('helLo world, eh?'))
print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter(''))
print(first_non_repeating_letter('aa'))


# codewars task best solution
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""


# codewars task best solution
from collections import Counter


def first_non_repeating_letter(string):
    cnt = Counter(string.lower())
    for letter in string:
        if cnt[letter.lower()] == 1:
            return letter
    return ''


# codewars task best solution
def first_non_repeating_letter(string):
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    return singles[0] if singles else ''


# codewars task best solution
def first_non_repeating_letter(string):

    s = string.lower()

    for i in string:
        if s.count(i.lower()) == 1:
            return i
    return ''


# codewars task best solution
def first_non_repeating_letter(string):
    for x in string:
        if string.lower().count(x.lower()) == 1:
            return x
    return ''


# codewars task best solution
def first_non_repeating_letter(string):
    return next((x for x in string if string.lower().count(x.lower()) == 1),
                '')


# codewars task best solution
def first_non_repeating_letter(string):
    for char in string:
        if string.lower().count(char.lower()) < 2:
            return char
    return ""