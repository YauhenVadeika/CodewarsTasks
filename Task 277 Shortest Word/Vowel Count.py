"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def find_short(s):

    return min([len(i) for i in s.split()])


print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(find_short("Let's travel abroad shall we"))


# codewars task best solution
def find_short(s):
    return min(len(x) for x in s.split())


# codewars task best solution
def find_short(s):
    return len(min(s.split(' '), key=len))


# codewars task best solution
def find_short(s):
    s = s.split()  # splits the string into a list of individual words
    l = min(s, key=len)  # finds the shortest string in the list
    return len(l)  # returns shortest word length


# codewars task best solution
def find_short(s):
    return min(map(len, s.split(' ')))


# codewars task best solution
def find_short(s):
    sList = s.split()
    shortestLength = len(sList[0])
    for item in sList:
        if len(item) < shortestLength:
            shortestLength = len(item)
    return shortestLength
