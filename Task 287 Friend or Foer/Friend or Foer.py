"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def friend(x):
    return [i for i in x if len(i) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))


# codewars task best solution
def friend(x):
    return [f for f in x if len(f) == 4]


# codewars task best solution
def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names


# codewars task best solution
def friend(x):
    return [i for i in x if len(i) == 4]


# codewars task best solution
def friend(x):
    myFriends = []  # Initialize list variable
    for person in x:  # Loop through list of names
        if len(person) == 4:  # Check to see if the name is of length 4
            myFriends.append(
                person
            )  # If the name is 4 characters long, append it to variable myFriends
    return myFriends  # Return myFriends list


# codewars task best solution
def friend(x):
    return filter(lambda name: len(name) == 4, x)