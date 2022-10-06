# my task solution
def remove_exclamation_marks(s):
    return ''.join([i for i in s if i != '!'])


print(remove_exclamation_marks("Hello World!"))
print(remove_exclamation_marks("Hello World!!!"))
print(remove_exclamation_marks("Hi! Hello!"))
print(remove_exclamation_marks(""))


# codewars task best solution
def remove_exclamation_marks(s):
    return s.replace('!', '')


# codewars task best solution
remove_exclamation_marks = lambda s: s.replace("!", "")
