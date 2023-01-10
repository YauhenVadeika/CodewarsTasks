# my task solution
def find_short(s):

    return min([len(i) for i in s.split()])


print(find_short("bitcoin take over the world maybe who knows perhaps"))
print(
    find_short(
        "turns out random test cases are easier than writing out basic ones"))
print(find_short("lets talk about javascript the best language"))
print(find_short("i want to travel the world writing code one day"))
print(find_short("Lets all go on holiday somewhere very cold"))
print(find_short("Let's travel abroad shall we"))


# codewars task best solution
def find_short(s):
    return min(len(x) for x in s.split())


# codewars task best solution
def find_short(s):
    return len(min(s.split(' '), key=len))


# codewars task best solution
def find_short(s):
    return min(map(len, s.split(' ')))


# codewars task best solution
def find_short(s):
    s = s.split()  # splits the string into a list of individual words
    l = min(s, key=len)  # finds the shortest string in the list
    return len(l)  # returns shortest word length


# codewars task best solution
def find_short(s):
    sList = s.split()
    shortestLength = len(sList[0])
    for item in sList:
        if len(item) < shortestLength:
            shortestLength = len(item)
    return shortestLength


# codewars task best solution
find_short = lambda s: min(len(e) for e in s.split())