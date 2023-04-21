"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def filter_list(l):
    return [i for i in l if type(i) is int]


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))


# codewars task best solution
def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]


# codewars task best solution
def filter_list(l):
    'return a new list with the strings filtered out'
    return [x for x in l if type(x) is not str]


# codewars task best solution
def filter_list(l):
    new_list = []
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list


# codewars task best solution
def filter_list(l):
    'return a new list with the strings filtered out'
    return [e for e in l if isinstance(e, int)]


# codewars task best solution
def filter_list(l):
    'return a new list with the strings filtered out'
    return [e for e in l if type(e) is int]
