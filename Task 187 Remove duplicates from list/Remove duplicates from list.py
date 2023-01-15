# my task solution
def distinct(seq):

    return list(dict.fromkeys(seq))


print(distinct([1, 1, 2]))
print(distinct([1, 1, 1, 2, 3, 4, 5, 1]))
print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))
print(
    distinct([
        4622911, 3658993, 3087079, 3116444, 3658993, 167228, 2288490, 3116444,
        250259, 3116444, 4075295, 3707970, 4779815, 3075730, 167228, 2085981,
        527724, 167228, 810623, 4115512, 1664641, 3075730, 1875696, 3116444,
        3658993, 1664641, 4543137, 180246, 3087079, 2958334, 2085981, 951191,
        3116444, 4047780, 4779815, 550422, 3075730, 4974415, 250259, 550422,
        4115512, 4779815, 2288490, 4779815, 3075730, 167228, 3116444, 4047780,
        180246, 3075730, 1994358, 1610096, 1610096, 2099263, 1608405, 2085981,
        715073, 4075295, 2085981, 3695759, 3877780, 77532, 527724, 3087079,
        3116444, 451390, 951191, 1664641, 3877780, 3116
    ]))


# codewars task best solution
def distinct(seq):
    return sorted(set(seq), key=seq.index)


# codewars task best solution
def distinct(seq):
    result = []
    seen = set()
    for a in seq:
        if a not in seen:
            result.append(a)
            seen.add(a)
    return result


# codewars task best solution
def distinct(seq):
    nl = []
    [nl.append(i) for i in seq if i not in nl]
    return nl


# codewars task best solution


def distinct(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)

    return result


# codewars task best solution
distinct = lambda s: [e for i, e in enumerate(s) if e not in s[:i]]
