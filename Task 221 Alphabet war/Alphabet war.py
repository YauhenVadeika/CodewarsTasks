# my task solution
def alphabet_war(fight):
    a, b = 'sbpw', 'zdqm'
    left, right = sum([a.find(i) + 1
                       for i in fight]), sum([b.find(j) + 1 for j in fight])
    return "Right side wins!" if left < right else "Left side wins!" if right < left else "Let's fight again!"


print(alphabet_war("zdqmwpbs"))
print(alphabet_war("zzzzs"))
print(alphabet_war("wwwwwwz"))


# codewars task best solution
def alphabet_war(fight):
    d = {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}
    r = sum(d[c] for c in fight if c in d)

    return {
        r == 0: "Let's fight again!",
        r > 0: "Left side wins!",
        r < 0: "Right side wins!"
    }[True]


# codewars task best solution
def alphabet_war(fight):
    result = sum("zdqm".find(c) - "sbpw".find(c) for c in fight)
    return "{} side wins!".format(
        "Left" if result < 0 else "Right") if result else "Let's fight again!"


# codewars task best solution
POWER = {
    # left side
    'w': -4,
    'p': -3,
    'b': -2,
    's': -1,
    # right side
    'm': 4,
    'q': 3,
    'd': 2,
    'z': 1
}


def alphabet_war(fight):
    result = sum(POWER.get(c, 0) for c in fight)
    return "Let's fight again!" if not result else \
          ["Left", "Right"][result > 0] + " side wins!"


# codewars task best solution
def alphabet_war(fight):
    left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    rigth = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    leftp = 0
    rigthp = 0
    for e in fight:
        leftp += left.get(e, 0)
        rigthp += rigth.get(e, 0)
    if leftp > rigthp:
        return 'Left side wins!'
    elif rigthp > leftp:
        return 'Right side wins!'
    else:
        return "Let's fight again!"


# codewars task best solution
def alphabet_war(fight):
    #your code here
    sum = 0
    for i in fight:
        if i == "w":
            sum = sum + 4
        elif i == "p":
            sum = sum + 3
        elif i == "b":
            sum = sum + 2
        elif i == "s":
            sum = sum + 1
        elif i == "m":
            sum = sum - 4
        elif i == "q":
            sum = sum - 3
        elif i == "d":
            sum = sum - 2
        elif i == "z":
            sum = sum - 1

    if sum > 0:
        return "Left side wins!"
    elif sum == 0:
        return "Let's fight again!"
    else:
        return "Right side wins!"