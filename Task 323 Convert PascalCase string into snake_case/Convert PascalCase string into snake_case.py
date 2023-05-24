"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def to_underscore(string):

    if string != str(string):
        return str(string)
    else:
        return "".join([
            '_' +
            string[i].lower() if string[i] != string[i].lower() else string[i]
            for i in range(len(string))
        ])[1::]


print(to_underscore("TestController"))
print(to_underscore("MoviesAndBooks"))
print(to_underscore("App7Test"))
print(to_underscore(1))

# codewars task best solution
import re


def to_underscore(string):
    return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()


# codewars task best solution
def to_underscore(string):
    string = str(string)
    camel_case = string[0].lower()
    for c in string[1:]:
        camel_case += '_{}'.format(c.lower()) if c.isupper() else c
    return camel_case


# codewars task best solution
def to_underscore(string):
    return ''.join('_' + c.lower() if c.isupper() else c
                   for c in str(string)).lstrip('_')


# codewars task best solution
def to_underscore(string):
    string = str(string)
    new = []
    for s in string:
        if not new:
            new.append(s)
        else:
            if s.isupper():
                new.append("_")
            new.append(s)
    return "".join(new).lower()


# codewars task best solution
import re


def to_underscore(string):
    return re.sub("(?<=.)(?=[A-Z])", "_", str(string)).lower()


# codewars task best solution
import re


def to_underscore(string):
    try:
        return '_'.join(x.lower() for x in re.findall('[A-Z][^A-Z]*', string))
    except:
        return str(string)


# codewars task best solution
def to_underscore(string):
    z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if type(string) == int:  # speical case
        return str(string)

    string = string.replace(string[0], string[0].lower())  # first letter
    ans = string  # so that string and len(string) remains the same
    for i in xrange(1, len(string)):  # start from the second letter
        if string[i] in z:
            ans = ans.replace(string[i], '_' + string[i].lower())
    return ans