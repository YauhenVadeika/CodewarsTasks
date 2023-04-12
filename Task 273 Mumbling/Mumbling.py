"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""

# my task solution, my second life


def accum(s):
    return "-".join([(s[i].ljust(j, s[i])).title()
                     for i, j in enumerate(range(1,
                                                 len(s) + 1))])


print(accum("abcd"))


# codewars task best solution
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


# codewars task best solution
def accum(s):
    output = ""
    for i in range(len(s)):
        output += (s[i] * (i + 1)) + "-"
    return output.title()[:-1]


# codewars task best solution
def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result) - 1]


# codewars task best solution
def accum(s):
    return '-'.join([c.upper() + c.lower() * i for i, c in enumerate(s)])


# codewars task best solution
def accum(s):
    str = ""
    for i in range(0, len(s)):
        str += s[i].upper()
        str += s[i].lower() * i
        if i != len(s) - 1:
            str += "-"
    return str