# My reasoning
# a = "Ooxx"
# a = "zpzpzpp"
# a = "xooxx"
# c = list(a.lower())
# d = c.count('o')
# e = c.count('x')
# if d == e or ('o' not in c and 'x' not in c):
#     print(True)
# else:
#     print(False)
####################################
# if 'o' not in c and 'x' not in c:
#     print(True)
#####################################


# my task solution
def xo(s):
    lst = list(s.lower())
    sumo = lst.count('o')
    sumx = lst.count('x')
    return True if sumo == sumx or ('o' not in lst and 'x' not in lst) else False


print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))

# codewars task best solution
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


# codewars task best solution
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
