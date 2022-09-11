# my task solution
def friend(x):
    lst = []
    [lst.append(i) for i in x if len(i) == 4]
    return lst


print(friend([
    "Ryan",
    "Kieran",
    "Mark",
]))
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))


# codewars task best solution
def friend(x):
    return [f for f in x if len(f) == 4]


# codewars task best solution
def friend(x):
    #Code
    names = []
    for name in x:
        if len(name) == 4:
            names.append(name)
    return names


# codewars task best solution
def friend(x):
    return filter(lambda name: len(name) == 4, x)