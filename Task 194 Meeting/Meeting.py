# my task solution
def meeting(s):
    return ''.join(
        sorted('({1}, {0})'.format(*(x.split(':')))
               for x in s.upper().split(';')))


print(
    meeting(
        "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
    ))


# codewars task best solution
def meeting(s):
    s = s.upper()
    s = s.split(';')
    array = []
    string = ""
    for i in s:
        i = i.split(':')
        string = '(' + i[1] + ', ' + i[0] + ')'
        array.append(string)
    array.sort()
    output = ""
    for j in array:
        output += j
    return output


# codewars task best solution
def meeting(s):
    return ''.join(f'({a}, {b})' for a, b in sorted(
        name.split(':')[::-1] for name in s.upper().split(';')))


# codewars task best solution
def meeting(s):
    s = s.split(";")
    s.sort()
    x = []
    for i in s:
        first = i.split(":")[0]
        last = i.split(":")[1]
        x.append(str("(" + last.upper() + ", " + first.upper() + ")"))
    x.sort()

    return ''.join(x)


# codewars task best solution
import re


def meeting(s):
    return "".join(
        sorted(re.sub("(\w+):(\w+);?", r"(\2, \1);", s.upper()).split(";")))


# codewars task best solution
meeting = lambda s: ''.join(
    sorted('(%s, %s)' % tuple(e.split(':')[::-1])
           for e in s.upper().split(';')))
