"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def ips_between(start, end):

    const = 256

    ipstart = [int(i) for i in (start.split('.'))]
    ipend = [int(i) for i in (end.split('.'))]
    # print(ipstart, ipend)
    resipstart = sum([(value * (const**(abs(index))))
                      for index, value in enumerate(ipstart, -3)])
    resipend = sum([(value * (const**(abs(index))))
                    for index, value in enumerate(ipend, -3)])
    # print(resipstart, resipend)
    return resipend - resipstart


print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("20.0.0.10", "20.0.1.0"))
print(ips_between("10.0.0.0", "10.0.1.0"))

# codewars task best solution
from ipaddress import ip_address


def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))


# codewars task best solution
def ips_between(start, end):
    a = sum([int(e) * 256**(3 - i) for i, e in enumerate(start.split('.'))])
    b = sum([int(e) * 256**(3 - i) for i, e in enumerate(end.split('.'))])
    return abs(a - b)


# codewars task best solution
from ipaddress import IPv4Address


def ips_between(start, end):
    return int(IPv4Address(end)) - int(IPv4Address(start))


# codewars task best solution
def ips_between(start, end):
    start, end = start.split('.'), end.split('.')
    pos0 = (int(end[0]) - int(start[0])) * (256**3)
    pos1 = (int(end[1]) - int(start[1])) * (256**2)
    pos2 = (int(end[2]) - int(start[2])) * 256
    pos3 = (int(end[3]) - int(start[3]))
    return pos0 + pos1 + pos2 + pos3


# codewars task best solution
def ips_between(start, end):
    return sum((int(b) - int(a)) * 256**i for i, (
        b, a) in enumerate(reversed(zip(end.split('.'), start.split('.')))))


# codewars task best solution
def ips_between(start, end):
    n1 = int(''.join(f'{n:08b}' for n in map(int, start.split('.'))), 2)
    n2 = int(''.join(f'{n:08b}' for n in map(int, end.split('.'))), 2)
    return n2 - n1


# codewars task best solution
def value(x):
    x = x.split('.')

    return int(x[0]) * 256**3 + int(x[1]) * 256**2 + int(x[2]) * 256 + int(
        x[3])


def ips_between(start, end):
    return value(end) - value(start)


# codewars task best solution
ips_between = lambda s, e: sum((int(i[0]) - int(i[1])) * j for i, j in zip(
    zip(e.split('.'), s.split('.')), [16777216, 65536, 256, 1]))


# codewars task best solution
def ips_between(start, end):
    # TODO
    difference = [
        int(b) - int(a) for a, b in zip(start.split("."), end.split("."))
    ]
    sum = 0
    for d in difference:
        sum *= 256
        sum += d
    return sum
