# my task solution
def pig_it(text):
    return ' '.join([
        f"{text.split(' ')[i][1:]+ text.split(' ')[i][0]+'ay'}"
        if text.split(' ')[i] not in '!.%&?' else text.split(' ')[i]
        for i in range(len(text.split(' ')))
    ])


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))


# my task solution
def pig_it(text):
    a = text.split(' ')
    return ' '.join([
        f"{a[i][1:]+ a[i][0]+'ay'}" if a[i] not in '!.%&?' else a[i]
        for i in range(len(a))
    ])


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))


# codewars task best solution
def pig_it(text):
    lst = text.split()
    return ' '.join([
        word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst
    ])


# codewars task best solution
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x
                    for x in text.split())


# codewars task best solution
def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)