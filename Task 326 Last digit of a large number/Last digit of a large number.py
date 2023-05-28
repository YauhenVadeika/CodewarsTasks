"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def last_digit(n1, n2):

    var = int(10)
    return pow(n1, n2, var)


print(last_digit(4, 1))
print(last_digit(9, 7))
print(last_digit(2**200, 2**300))
print(
    last_digit(3715290469715693021198967285016729344580685479654510946723,
               68819615221552997273737174557165657483427362207517952651))


# codewars task best solution
def last_digit(n1, n2):
    return pow(n1, n2, 10)


# codewars task best solution
def last_digit(n1, n2):
    return (n1 % 10)**(n2 % 4 + 4 * bool(n2)) % 10


# codewars task best solution
def last_digit(n1, n2):
    m1 = n1 % 10
    if m1 == 1:
        return 1
    if m1 == 2:
        if n2 == 0:
            return 1
        elif n2 % 4 == 3:
            return 8
        elif n2 % 4 == 0:
            return 6
        elif n2 % 4 == 2:
            return 4
        else:
            return 2
    if m1 == 3:
        if n2 == 0:
            return 1
        elif n2 % 4 == 0:
            return 1
        elif n2 % 2 == 0:
            return 9
        elif n2 % 4 == 3:
            return 7
        else:
            return 3
    if m1 == 4:
        if n2 == 0:
            return 1
        elif n2 % 4 == 2 or n2 % 4 == 0:
            return 6
        else:
            return 4
    if m1 == 5:
        if n2 == 0:
            return 1
        else:
            return 5
    if m1 == 6:
        if n2 == 0:
            return 1
        else:
            return 6
    if m1 == 7:
        if n2 == 0:
            return 1
        elif n2 % 4 == 3:
            return 3
        elif n2 % 4 == 0:
            return 1
        elif n2 % 4 == 2:
            return 9
        else:
            return 7
    if m1 == 8:
        if n2 == 0:
            return 1
        elif n2 % 4 == 3:
            return 2
        elif n2 % 4 == 0:
            return 6
        elif n2 % 4 == 2:
            return 4
        else:
            return 8
    if m1 == 9:
        if n2 == 0:
            return 1
        elif n2 % 2 == 1:
            return 9
        else:
            return 1
    if m1 == 0:
        if n2 == 0:
            return 1
        return 0


# codewars task best solution
E = [[0, 0, 0, 0], [1, 1, 1, 1], [6, 2, 4, 8], [1, 3, 9, 7], [6, 4, 6, 4],
     [5, 5, 5, 5], [6, 6, 6, 6], [1, 7, 9, 3], [6, 8, 4, 2], [1, 9, 1, 9]]


def last_digit(n1, n2):
    if n2 == 0: return 1
    return E[n1 % 10][n2 % 4]


# codewars task best solution
digits = {
    0: [0, 0, 0, 0],
    1: [1, 1, 1, 1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6, 4, 6],
    5: [5, 5, 5, 5],
    6: [6, 6, 6, 6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1, 9, 1]
}


def last_digit(n1, n2):
    return digits[n1 % 10][(n2 - 1) % 4] if n2 else 1


# codewars task best solution
def last_digit(n1, n2):
    last_dict = {
        0: [0],
        1: [1],
        2: [2, 4, 6, 8],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    if n2 == 0:
        return 1
    a = n1 % 10
    return last_dict[a][(n2 - 1) % len(last_dict[a])]


# codewars task best solution
def last_digit(n1, n2):
    return 1 if n2 == 0 else pow(n1 % 10, 1 + (n2 - 1) % 4, 10)


# codewars task best solution
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    n1 %= 10
    if n1 in [0, 1, 5, 6]:
        return n1
    if n1 == 2:
        return [6, 2, 4, 8][n2 % 4]
    if n1 == 3:
        return [1, 3, 9, 7][n2 % 4]
    if n1 == 4:
        return [6, 4][n2 % 2]
    if n1 == 7:
        return [1, 7, 9, 3][n2 % 4]
    if n1 == 8:
        return [6, 8, 4, 2][n2 % 4]
    return [1, 9][n2 % 2]


# codewars task best solution
def last_digit(n1, n2):
    if n2 == 0: return 1
    seq = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6],
           [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
    l_digit = int(str(n1)[-1])
    position = n2 % len(seq[l_digit])
    return seq[l_digit][position - 1]