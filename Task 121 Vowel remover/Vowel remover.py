# my task solution
def shortcut(s):
    return "".join([i for i in s if i not in "aeiou"])


print(shortcut("hello"))
print(shortcut("codewars"))
print(shortcut("goodbye"))
print(shortcut("HELLO"))


# codewars task best solution
def shortcut(s):
    return s.translate(None, 'aeiou')


# codewars task best solution
def shortcut(s):
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s
