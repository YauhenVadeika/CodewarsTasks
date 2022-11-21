# my task solution
def solve(s):
    return (s.lower, s.upper)[sum(map(str.isupper, s)) > len(s) / 2]()


print(solve("coDe"))  # --> code
print(solve("CODe"))  # --> CODE
print(solve("coDE"))  # --> code
print(solve("Code"))  # --> code


# codewars task best solution
def solve(s):
    upper = 0
    lower = 0

    for char in s:
        if char.islower():
            lower += 1
        else:
            upper += 1

    if upper == lower or lower > upper:
        return s.lower()
    else:
        return s.upper()


# codewars task best solution
def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()


# codewars task best solution
def solve(s):
    lower_case = [l for l in s if l.islower()]
    upper_case = [l for l in s if l.isupper()]

    if len(upper_case) > len(lower_case):
        return s.upper()
    return s.lower()