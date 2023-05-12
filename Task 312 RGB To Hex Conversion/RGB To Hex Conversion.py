"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def rgb(r, g, b):

    arr = []

    for i in (r, g, b):
        if i > 255:
            arr.append(f"{255:02x}".upper())
        elif i < 0:
            arr.append("00")
        else:
            arr.append(f"{i:02x}".upper())
    return ''.join(arr)


print(rgb(255, 255, 255))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))
print(rgb(1, 2, 3))
print(rgb(3, -2, -3))


# codewars task best solution
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


# codewars task best solution
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))


# codewars task best solution
def rgb(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))


# codewars task best solution
def hex_con(color):
    hex_dict = '0123456789ABCDEF'
    d1 = color // 16
    d2 = color % 16
    if d1 > 15:
        d1 = 15
        d2 = 15
    elif d1 < 0:
        d1 = 0
        d2 = 0
    return str(hex_dict[d1]) + str(hex_dict[d2])


def rgb(r, g, b):
    R = hex_con(r)
    G = hex_con(g)
    B = hex_con(b)
    return R + G + B


# codewars task best solution
def rgb(r, g, b):
    return ''.join(['%02X' % max(0, min(x, 255)) for x in [r, g, b]])