# my task solution
def no_odds(values):
    return [i for i in values if i % 2 == 0]


print(no_odds([0, 1]))


# codewars task best solution
def no_odds(values):
    return [i for i in values if i % 2 == 0]


# codewars task best solution
def no_odds(values):
    return [x for x in values if not x % 2]


# codewars task best solution
def no_odds(values):
    list = []
    for i in values:
        if i % 2 == 0:
            list.append(i)
    return list


# codewars task best solution
def no_odds(values):
    # Return list of only even values
    return list(filter(lambda x: x % 2 == 0, values))


# codewars task best solution
def no_odds(values):
    return [x for x in values if x & 1 ^ 1]
