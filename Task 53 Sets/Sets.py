# my task solution
def sets(lst):
    res = list(set(lst))
    res.sort()
    return res


lst = [1, 1, 5, 4, 9, 7, 4, 5, 8, 3, 9]
print(sets(lst))
