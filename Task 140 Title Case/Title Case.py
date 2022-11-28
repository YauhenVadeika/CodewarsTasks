# my task solution
def title_case(title, minor_words=''):

    return " ".join([
        i.title() if i not in minor_words.lower().split() or j == 0 else i
        for j, i in enumerate(title.lower().split())
    ])


print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))


# codewars task best solution
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join(
        [word if word in minor_words else word.capitalize() for word in title])


# codewars task best solution
def title_case(title, minor_words=''):
    title, minor_words = title.lower().split(), minor_words.lower().split()
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    return ' '.join(title)


# codewars task best solution
def title_case(title, minor_words=''):
    return ' '.join(
        w if w in minor_words.lower().split() and i else w.capitalize()
        for i, w in enumerate(title.lower().split()))


# codewars task best solution
def title_case(title, minor_words=''):
    return ' '.join(c if c in minor_words.lower().split() else c.title()
                    for c in title.capitalize().split())
