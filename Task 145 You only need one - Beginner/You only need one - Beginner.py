# my task solution
def check(seq, elem):
    return True if elem in seq else False


print(check([66, 101], 66))
print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))
print(check([101, 45, 75, 105, 99, 107], 107))
print(check([66, "codewars", 11, "alex loves pushups"], "alex loves pushups"))

# codewars task best solution
def check(seq, elem):
    return elem in seq


# codewars task best solution
def check(list, x):
    while True:
        if x in list:
            return True
        else:
            return False
    pass


# codewars task best solution
check = lambda seq, elem: elem in seq
