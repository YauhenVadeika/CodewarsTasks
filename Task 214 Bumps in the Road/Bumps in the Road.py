# my task solution
def bumps(road):
    return "Woohoo!" if road.count('n') <= 15 else "Car Dead"


print(bumps('__nn_nnnn__n_n___n____nn__nnn'))


# codewars task best solution
def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"


# codewars task best solution
def bumps(road):
    if road.count('n') > 15:
        return "Car Dead"
    else:
        return "Woohoo!"


# codewars task best solution
bumps = lambda s: ["Woohoo!", "Car Dead"][s.count('n') > 15]
# codewars task best solution
from collections import Counter


def bumps(road):
    return "Car Dead" if Counter(road)['n'] > 15 else "Woohoo!"


# codewars task best solution
import re


def bumps(road):
    return "Woohoo!" if len(re.findall("n", road)) < 16 else "Car Dead"