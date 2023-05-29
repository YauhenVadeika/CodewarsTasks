"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""

# my task solution, my second life


def hex_string_to_RGB(hex_string):

    lstrp = hex_string.lstrip('#')
    n = 2

    red, green, blue = [
        int(lstrp[i:i + n], 16) for i in range(0, len(lstrp), n)
    ]
    return {'r': red, 'g': green, 'b': blue}


print(hex_string_to_RGB("#FF9933"))
print(hex_string_to_RGB("#ff9900"))
print(hex_string_to_RGB("#AB9922"))


# codewars task best solution
def hex_string_to_RGB(hex):
    return {
        'r': int(hex[1:3], 16),
        'g': int(hex[3:5], 16),
        'b': int(hex[5:7], 16)
    }


# codewars task best solution
def hex_string_to_RGB(hex_string):
    # your code here
    r = int(hex_string[1:3], 16)
    g = int(hex_string[3:5], 16)
    b = int(hex_string[5:7], 16)

    return {'r': r, 'g': g, 'b': b}


# codewars task best solution
def hex_string_to_RGB(s):
    return {i: int(s[j:j + 2], 16) for i, j in zip('rgb', [1, 3, 5])}


# codewars task best solution
def hex_string_to_RGB(s):
    return {c: int(s[1 + 2 * i:3 + 2 * i], 16) for i, c in enumerate('rgb')}


# codewars task best solution
from PIL import ImageColor


def hex_string_to_RGB(hex_string):
    rgb = ImageColor.getrgb(hex_string)
    res = {'r': rgb[0], 'g': rgb[1], 'b': rgb[2]}
    return res


# codewars task best solution
def hex_string_to_RGB(hex_string):
    hex_string = hex_string.replace("#", "")
    hexd = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "A": "10",
        "B": "11",
        "C": "12",
        "D": "13",
        "E": "14",
        "F": "15",
        "a": "10",
        "b": "11",
        "c": "12",
        "d": "13",
        "e": "14",
        "f": "15"
    }
    return {
        "r": int(hexd[hex_string[0]]) * 16 + int(hexd[hex_string[1]]),
        "g": int(hexd[hex_string[2]]) * 16 + int(hexd[hex_string[3]]),
        "b": int(hexd[hex_string[4]]) * 16 + int(hexd[hex_string[5]])
    }


# codewars task best solution
def hex_string_to_RGB(hex_string):
    r, g, b = [int(hex_string[i:i + 2], 16) for i in (1, 3, 5)]
    return {'r': r, 'g': g, 'b': b}


# codewars task best solution
def hex_string_to_RGB(hex_string):
    return {
        s: int(hex_string[i:i + 2], 16)
        for s, i in zip('rgb', range(1, 7, 2))
    }


# codewars task best solution
def hex_string_to_RGB(hex_string):
    return {
        'r': int(f'0x{hex_string[1:3]}', 16),
        'g': int(f'0x{hex_string[3:5]}', 16),
        'b': int(f'0x{hex_string[5:]}', 16)
    }


# codewars task best solution
def hex_string_to_RGB(h):

    def hex(_h):
        return int(_h, 16)

    return {'r': hex(h[1:3]), 'g': hex(h[3:5]), 'b': hex(h[5:7])}


# codewars task best solution
def hexToInt(hex_string):
    return int(hex_string, 16)


def hex_string_to_RGB(hex_string):
    return {
        'r': hexToInt(hex_string[1:3]),
        'g': hexToInt(hex_string[3:5]),
        'b': hexToInt(hex_string[5:])
    }