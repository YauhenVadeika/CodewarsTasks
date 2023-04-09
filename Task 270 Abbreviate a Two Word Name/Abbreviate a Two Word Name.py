"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def abbrev_name(name):
    return ".".join([i.title()[0] for i in name.split()])


print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))


# codewars task best solution
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


# codewars task best solution
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]


# codewars task best solution
def abbrevName(name):
    return name.split(' ')[0][0].upper() + '.' + name.split(' ')[1][0].upper()


# codewars task best solution
def abbrevName(name):
    names = name.split()
    return f"{names[0][0]}.{names[1][0]}".upper()


# codewars task best solution
def abbrevName(name):
    return '.'.join(x[0].upper() for x in name.split())