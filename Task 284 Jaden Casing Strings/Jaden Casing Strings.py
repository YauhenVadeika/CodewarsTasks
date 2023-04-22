"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def to_jaden_case(string):
    return " ".join([i.capitalize() for i in string.split()])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# codewars task best solution
import string

toJadenCase = string.capwords


# codewars task best solution
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


# codewars task best solution
def to_jaden_case(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)


# codewars task best solution
def to_jaden_case(string):
    words = string.split(" ")
    output = ""
    for word in words:
        corrected = word.capitalize()
        output += corrected + " "

    return output[0:-1]


# [0:-1] to take from begining to last one excluding the last one " "
# word.capitalize = to capitalize the first letter of an string
# codewars task best solution
def to_jaden_case(string):
    return ' '.join(map(str.capitalize, string.split()))


# codewars task best solution
def to_jaden_case(string):
    return ' '.join([x.capitalize() for x in string.split()])