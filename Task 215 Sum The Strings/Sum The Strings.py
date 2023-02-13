# my task solution
def sum_str(a, b):

    if a and b:
        return str(int(a) + int(b))
    if a:
        return a
    if b:
        return b
    if a == "" and b == "":
        return '0'


print(sum_str("-5", "3"))
print(sum_str("-5", ""))
print(sum_str("", "6"))
print(sum_str("", ""))


# codewars task best solution
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


# codewars task best solution
def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))


# codewars task best solution
def sum_str(a, b):
    print(a, b)
    if a == "" or a == None: a = "0"
    if b == "" or b == None: b = "0"
    return str(int(a) + int(b))


# codewars task best solution
def sum_str(a, b):
    if a == '': a = '0'
    if b == '': b = '0'
    return str(int(a) + int(b))


# codewars task best solution
def sum_str(*values):
    return str(sum(int(s or '0') for s in values))
