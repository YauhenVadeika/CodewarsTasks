# my task solution
def get_middle(s):
    return s[(len(s) // 2) - 1] + s[len(s) // 2] if len(s) % 2 == 0 else s[(len(s) // 2)]


print(get_middle("testing"))
print(get_middle("test"))
print(get_middle("A"))
print(get_middle("middle"))
print(get_middle("of"))


# codewars task best solution
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


# codewars task best solution
import math
def get_middle(s):
    #your code here
    x = len(s)
    y = int(x / 2)
    if x % 2 == 0:
        return s[y - 1:y + 1]
    else:
        return s[y:y + 1]


# codewars task best solution
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s


# codewars task best solution
def get_middle(s):
    a = len(s)
    if len(s) == 1:
        return s
    elif len(s) % 2 == 0:
        return s[int(a / 2) - 1] + s[int(a / 2)]
    else:
        return s[int(a / 2)]
