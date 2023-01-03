# my task solution
def get_volume_of_cuboid(length, width, height):
    return int(length * width * height)


print(get_volume_of_cuboid(1, 2, 2))
print(get_volume_of_cuboid(6.3, 2, 5))

# codewars task best solution
from functools import reduce


def get_volume_of_cuboid(*args):
    return int(reduce(lambda x, y: x * y, args))


# codewars task best solution
import math


def get_volume_of_cuboid(*vol):
    return math.prod(vol)


# codewars task best solution
get_volume_of_cuboid = lambda x, y, z: x * y * z


# codewars task best solution
def get_volume_of_cuboid(*x):

    v = 1

    for i in x:
        v *= i
    return v
