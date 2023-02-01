# my task solution
def maskify(cc):
    return cc if len(cc) < 5 else cc[-4:].rjust(len(cc), '#')


print(maskify('SF$SDfgsd2eA'))
print(maskify('123'))
print(maskify(''))

# codewars task best solution
def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]


# codewars task best solution
def maskify(cc):
    l = len(cc)
    if l <= 4: return cc
    return (l - 4) * '#' + cc[-4:]


# codewars task best solution
def maskify(cc):
    return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))


# codewars task best solution
def maskify(cc):

    word = list(cc)
    #loop through the list except the last 4 index's this will also prevent
    #the loop from running for anything less than 5 index's long
    for i in range(len(word) - 4):
        word[i] = '#'
    # join and return the list
    return ''.join(word)
    pass


# codewars task best solution
def maskify(cc):
    return cc[-4:].rjust(len(cc), "#")


# codewars task best solution
def maskify(cc):
    width = len(cc)
    return cc[-4:].rjust(width, '#')
