# my task solution
def replace_exclamation(s):
    return "".join(
        ["!" if i in "aeiou" or i in "aeiou".upper() else i for i in s])


print(replace_exclamation("Hi!"))
print(replace_exclamation("!Hi! Hi!"))
print(replace_exclamation("ABCDE"))


# codewars task best solution
def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


# codewars task best solution
def replace_exclamation(s):
    return s.translate(str.maketrans('aeiouAEIOU', '!' * 10))


# codewars task best solution
def replace_exclamation(s):
    for i in "aeuioAEUIO":
        s = s.replace(i, "!")
    return s


# codewars task best solution
replace_exclamation = lambda s: ''.join("!" if c in "aiueoAIUEO" else c for c in s)
