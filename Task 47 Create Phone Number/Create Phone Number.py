# my task solution
def create_phone_number(n):
    res = "".join([str(i) for i in n])
    return f"({res[:3]}) {res[3:6]}-{res[6:]}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]))


# codewars task best solution
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


# codewars task best solution
def create_phone_number(n):
    str1 = ''.join(str(x) for x in n[0:3])
    str2 = ''.join(str(x) for x in n[3:6])
    str3 = ''.join(str(x) for x in n[6:10])
