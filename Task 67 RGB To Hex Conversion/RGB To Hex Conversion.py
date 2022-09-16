# my task solution
def rgb(r, g, b):
    return ('{:02x}' * 3).format(*map(lambda var: max(0, min(255, var)), (r, g, b))).upper()


print(rgb(-20, 275, 125))
print(rgb(0, 0, 0))
print(rgb(255, 255, 255))


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