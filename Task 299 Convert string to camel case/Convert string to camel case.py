"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def to_camel_case(text):
    arr = "".join([i if i.isalpha() else " " for i in text]).split()
    return "".join([j.title() if j != arr[0] else j for j in arr])


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))


# codewars task best solution
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])


# codewars task best solution
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


# codewars task best solution
import re


def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)


# codewars task best solution
def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])


# codewars task best solution
def to_camel_case(text):
    cap = False
    newText = ''
    for t in text:
        if t == '_' or t == '-':
            cap = True
            continue
        else:
            if cap == True:
                t = t.upper()
            newText = newText + t
            cap = False
    return newText


# codewars task best solution
from re import compile as reCompile

PATTERN = reCompile(r'(?i)[-_]([a-z])')


def to_camel_case(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)


# codewars task best solution
def to_camel_case(text):
    return text[0] + ''.join(
        [w[0].upper() + w[1:]
         for w in text.replace("_", "-").split("-")])[1:] if text else ''
