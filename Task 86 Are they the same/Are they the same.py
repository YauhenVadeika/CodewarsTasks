# my task solution
def comp(array1, array2):

    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    array1.sort(key=abs)
    array2.sort(key=abs)
    return all(a**2 == b for a, b in zip(array1, array2))


print(
    comp([121, 144, 19, 161, 19, 144, 19, 11],
         [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))


# codewars task best solution
def comp(array1, array2):
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False


# codewars task best solution
def comp(a1, a2):
    return None not in (a1, a2) and [i * i for i in sorted(a1)] == sorted(a2)


# codewars task best solution
def comp(array1, array2):
    if array1 and array2:
        return sorted([x * x for x in array1]) == sorted(array2)
    return array1 == array2 == []


# codewars task best solution
def comp(a1, a2):
    return isinstance(a1, list) and isinstance(a2, list) and sorted(x * x for x in a1) == sorted(a2)
