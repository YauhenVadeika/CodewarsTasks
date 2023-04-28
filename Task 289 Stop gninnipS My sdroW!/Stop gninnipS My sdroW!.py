"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def spin_words(sentence):
    return " ".join(
        [i[::-1] if len(i) > 4 else i for i in sentence.split(" ")])


print(spin_words("Hey fellow warriors"))
print(spin_words("Welcome"))


# codewars task best solution
def spin_words(sentence):
    # Your code goes here
    return " ".join(
        [x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


# codewars task best solution
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)


# codewars task best solution
def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string


# codewars task best solution
def spin_words(sentence):
    return ' '.join(word if len(word) < 5 else word[::-1]
                    for word in sentence.split())


# codewars task best solution
def spin_words(sentence):
    words = sentence.split()
    output = []
    delimiter = " "
    for word in words:
        if len(word) >= 5:
            output.append(reverse(word))
        else:
            output.append(word)
    return delimiter.join(output)


def reverse(string):
    return string[::-1]


# codewars task best solution
import re


def spin_words(sentence):
    # Your code goes here
    return re.sub(r"\w{5,}", lambda w: w.group(0)[::-1], sentence)