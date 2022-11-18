# my task solution
def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    lst = text.split()
    return "".join([i.capitalize() if i != lst[0] else i for i in lst])


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))


# codewars task best solution
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


# codewars task best solution
def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])


# codewars task best solution
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])


# codewars task best solution
def to_camel_case(text):
    return "".join([
        i if n == 0 else i.capitalize()
        for n, i in enumerate(text.replace("-", "_").split("_"))
    ])
