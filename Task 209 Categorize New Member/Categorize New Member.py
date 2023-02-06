# my task solution
def open_or_senior(data):

    return ["Senior" if i[0] >= 55 and i[1] > 7 else "Open" for i in data]


print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]))
print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78,
                                                                       9]]))


def open_or_senior(data):

    array = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            array.append("Senior")
        else:
            array.append("Open")
    return array


print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]))
print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78,
                                                                       9]]))


# codewars task best solution
def openOrSenior(data):
    return [
        "Senior" if age >= 55 and handicap >= 8 else "Open"
        for (age, handicap) in data
    ]


# codewars task best solution
def openOrSenior(data):
    res = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    return res


# codewars task best solution
def openOrSenior(members):
    return ["Senior" if m[0] > 54 and m[1] > 7 else "Open" for m in members]


# codewars task best solution
def openOrSenior(data):
    return [
        "Senior" if age >= 55 and handicap > 7 else "Open"
        for age, handicap in data
    ]


# codewars task best solution
def openOrSenior(data):
    list = []
    for age, hcap in data:

        if age >= 55 and hcap > 7:
            list.append('Senior')

        else:
            list.append('Open')

    return list