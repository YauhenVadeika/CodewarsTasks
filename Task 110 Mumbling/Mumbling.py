# my task solution
def accum(s):
    return '-'.join([f"{(s[i]*(i+1)).title()}" for i in range(len(s))])


print(accum("abcd"))
print(accum("RqaEzty"))


# codewars task best solution
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


# codewars task best solution
def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))


# codewars task best solution
def accum(s):
    output = ""
    for i in range(len(s)):
        output += (s[i] * (i + 1)) + "-"
    return output.title()[:-1]