"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def array_diff(a, b):
    return [var for var in a if var not in b]


print(array_diff([1, 2], [1]))  # --> [2]
print(array_diff([1, 2, 3], [1, 2]))
print(array_diff([], [1, 2]))
print(array_diff([1, 2, 2], []))
print(array_diff([1, 2, 2], [1]))  # -->[2,2]


# codewars task best solution
def array_diff(a, b):
    return [x for x in a if x not in b]


# codewars task best solution
def array_diff(a, b):
    return [x for x in a if x not in set(b)]


# codewars task best solution
def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]


# codewars task best solution
def array_diff(a, b):
    #your code here
    return filter(lambda i: i not in b, a)


# codewars task best solution
def array_diff(a, b):
    #your code here
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a


# codewars task best solution
def array_diff(a, b):
    return [v for v in a if v not in b]


# codewars task best solution
def array_diff(a, b):
    for n in b:
        while (n in a):
            a.remove(n)
    return a


# codewars task best solution
def array_diff(a, b):
    return [i for i in a if i not in b]
