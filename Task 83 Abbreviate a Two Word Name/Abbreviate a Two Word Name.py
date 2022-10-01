# my task solution
def abbrev_name(name):
    return ''.join([i for i in name.replace(' ', '.').title() if i == i.upper()])


print(abbrev_name("patrick feenan"))
print(abbrev_name("Sam Harris"))
print(abbrev_name("Evan C"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))


# codewars task best solution
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


# codewars task best solution
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]


# codewars task best solution
def abbrevName(name):
    return name.split(' ')[0][0].upper()+'.'+name.split(' ')[1][0].upper()