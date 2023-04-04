"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def solution(string):
    return string[::-1]


print(solution('world'))
print(solution(''))


# codewars task best solution
def solution(str):
    return str[::-1]


# codewars task best solution
def solution(string):
    return string[::-1]


# codewars task best solution
def solution(string):
    # Pythonic way :)
    return string[::-1]

    # For beginners it's good practise
    # to know how reverse() or [::-1]
    # works on the surface
    #for char in range(len(string)-1,-1,-1):
    #return string[char]


# codewars task best solution
def solution(s):
    return s[::-1]


# codewars task best solution
def solution(string):
    newstring = ""
    letter = len(string) - 1
    for x in string:
        x = string[letter]
        newstring = newstring + x
        letter = letter - 1
    return newstring