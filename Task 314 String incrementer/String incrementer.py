"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def increment_string(strng):

    endstr = strng.rstrip("".join([chr(i) for i in range(48, 58)]))
    startstr = strng[len(endstr):]
    if startstr == "":
        return strng + "1"
    return endstr + str(int(startstr) + 1).zfill(len(startstr))


print(increment_string(""))
print(increment_string("foo"))
print(increment_string("foobar1"))
print(increment_string("fo99obar99"))
print(increment_string("foobar001"))


# codewars task best solution
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


# codewars task best solution
def increment_string(strng):

    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')

    # get the part of strng that was stripped
    ints = strng[len(stripped):]

    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)

        # add 1 to ints
        new_ints = 1 + int(ints)

        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)

        return stripped + new_ints


# codewars task best solution
import re


def increment_string(input):
    match = re.search("(\d*)$", input)
    if match:
        number = match.group(0)
        if number is not "":
            return input[:-len(number)] + str(int(number) + 1).zfill(
                len(number))
    return input + "1"


# codewars task best solution
import re


def increment_string(strng):
    m = re.match('^(.*?)(\d+)$', strng)
    name, num = (m.group(1), m.group(2)) if m else (strng, '0')
    return '{0}{1:0{2}}'.format(name, int(num) + 1, len(num))


# codewars task best solution
def increment_string(s):
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))

    return s + "1"


# codewars task best solution
def increment_string(s):
    c = s.rstrip('0123456789')
    n = s[len(c):]
    if n == '':
        return s + '1'
    else:
        return c + str(int(n) + 1).zfill(len(n))


# codewars task best solution
increment_string = f = lambda s: s and s[-1].isdigit() and (f(
    s[:-1]) + "0", s[:-1] + str(int(s[-1]) + 1))[s[-1] < "9"] or s + "1"

# codewars task best solution
import re


def increment_string(s):
    number = re.findall(r'\d+', s)
    if number:
        s_number = number[-1]
        s = s.rsplit(s_number, 1)[0]
        number = str(int(s_number) + 1)
        return s + '0' * (len(s_number) - len(number)) + number
    return s + '1'