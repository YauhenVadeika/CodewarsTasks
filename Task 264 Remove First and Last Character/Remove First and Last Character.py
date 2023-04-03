"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def remove_char(s):
    return s[1:-1]


print(remove_char('eloquent'))


# codewars task best solution
def remove_char(s):
    return s[1:-1]


# codewars task best solution
def remove_char(s):
    return '' if len(s) <= 2 else s[1:-1]


# codewars task best solution
def remove_char(s):
    return s[1:len(s) - 1]


# codewars task best solution
def remove_char(s):
    if s == "eloquent":  #confirming the s variable equals the word "eloquent"
        return (
            s[1:7]
        )  #telling the program if s is "eloquent" print all except first and last letters
    elif s == "country":  #confirming the s variable equals the word "country"
        return (
            s[1:6]
        )  #telling the program if s is "country" print all except first and last
    elif s == "person":  #same as 1,3
        return (s[1:5])  #same as 2,4
    elif s == "place":  #same as 1,3
        return (s[1:4])  #same as 2,4
    elif s == "ok":  #same as 1,3
        return ""  #telling the program if s is "ok" don't print anything, ok is only 2 letters
    else:  #if anything else is entered,
        return (
            s[1:-1]
        )  #tell the program s is the input without the first and last characters


# codewars task best solution
remove_char = lambda s: s[1:-1]


# codewars task best solution
def remove_char(s):
    s = list(s)
    s.pop()
    s.pop(0)
    return ''.join(s)
