def disemvowel(st):
    return "".join([i for i in st if i not in "aeiouAEIOU"])


print(disemvowel("This website is for losers LOL!"))


# codewars task best solution
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


# codewars task best solution
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')
    return s


# codewars task best solution
import re


def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags=re.IGNORECASE)


# codewars task best solution