"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def get_count(sentence):
    return sum([1 if i in "aeiou" else 0 for i in sentence])


print(get_count("aeiou"))
print(get_count("abracadabra"))


# codewars task best solution
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


# codewars task best solution
def getCount(s):
    return sum(c in 'aeiou' for c in s)


# codewars task best solution
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels


# codewars task best solution
import re


def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))


# codewars task best solution
def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])


# codewars task best solution
def getCount(inputStr):
    return len([x for x in inputStr if x in 'aeoiu'])
