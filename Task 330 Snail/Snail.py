"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def snail(snail_map):

    i = len(snail_map)
    j = len(snail_map[0])

    if i == j:
        tab = []
        while snail_map:
            tab.extend(list(snail_map.pop(0)))
            snail_map = list(zip(*snail_map))
            snail_map.reverse()
        return tab
    else:
        return [[]]


print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(snail([[]]))

# codewars task best solution
import numpy as np


def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m


# codewars task best solution
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret


# codewars task best solution
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1]  # Rotate
    return out


# codewars task best solution
# my implementation/explanation of the solution by foxxyz
def snail(array):
    if array:
        # force to list because zip returns a list of tuples
        top_row = list(array[0])
        # rotate the array by switching remaining rows & columns with zip
        # the * expands the remaining rows so they can be matched by column
        rotated_array = zip(*array[1:])
        # then reverse rows to make the formerly last column the next top row
        rotated_array = rotated_array[::-1]
        return top_row + snail(rotated_array)
    else:
        return []


# codewars task best solution
def snail(array):
    mission = Game(array)
    path = []
    while mission.we_are_not_done:
        path.append(mission.dig_at_location())
        if mission.it_is_safe_to_slither:
            mission.slither_onwards_good_soldier()
        else:
            mission.turn_away_from_fire()
            mission.slither_onwards_good_soldier()
    return path


class Game(object):

    def __init__(self, array):
        self.map = array
        self.moves_left = len(array) * len(array[0])
        self.coords = {"x": 0, "y": len(array) - 1}  # start in NW area.
        self.dir = "E"  # slitherin' east.
        self.fire = {
            "min_x": -1,
            "min_y": -1,
            "max_x": len(array),
            "max_y": len(array)
        }  # the carpet is lava.
        self.rules = {
            "N": {
                "x": 0,
                "y": 1,
                "turn": "E"
            },
            "E": {
                "x": 1,
                "y": 0,
                "turn": "S"
            },
            "S": {
                "x": 0,
                "y": -1,
                "turn": "W"
            },
            "W": {
                "x": -1,
                "y": 0,
                "turn": "N"
            }
        }

    def slither_onwards_good_soldier(self):
        self.coords["x"] = self.next_x
        self.coords["y"] = self.next_y
        self._subtract_move()

    def turn_away_from_fire(self):
        self._become_aware_that_the_world_is_closing_in()
        self.dir = self.rules[self.dir]["turn"]

    def dig_at_location(self):
        # have to invert the y location for the purpose of the array.
        return self.map[len(self.map) - self.coords["y"] - 1][self.coords["x"]]

    def report_in(self):
        print("Dear Sir! I'm stationed @ x: %s, y: %s, heading %s." %
              (self.coords["x"], self.coords["y"], self.dir))

    @property
    def it_is_safe_to_slither(self):
        x = self.next_x
        y = self.next_y
        if x != self.fire["min_x"] and \
           x != self.fire["max_x"] and \
           y != self.fire["min_y"] and \
           y != self.fire["max_y"]:
            return True

    @property
    def we_are_not_done(self):
        if self.moves_left > 0:
            return True

    @property
    def next_x(self):
        return self.coords["x"] + self.rules[self.dir]["x"]

    @property
    def next_y(self):
        return self.coords["y"] + self.rules[self.dir]["y"]

    def _become_aware_that_the_world_is_closing_in(self):
        if self.dir == "N":
            self.fire["min_x"] += 1
        if self.dir == "E":
            self.fire["max_y"] -= 1
        if self.dir == "S":
            self.fire["max_x"] -= 1
        if self.dir == "W":
            self.fire["min_y"] += 1

    def _subtract_move(self):
        self.moves_left -= 1


# codewars task best solution
def snail(array):
    next_dir = {"right": "down", "down": "left", "left": "up", "up": "right"}
    dir = "right"
    snail = []
    while array:
        if dir == "right":
            snail.extend(array.pop(0))
        elif dir == "down":
            snail.extend([x.pop(-1) for x in array])
        elif dir == "left":
            snail.extend(list(reversed(array.pop(-1))))
        elif dir == "up":
            snail.extend([x.pop(0) for x in reversed(array)])
        dir = next_dir[dir]
    return snail


# codewars task best solution
import numpy as np


def snail(array):
    arr = np.array(array)

    if len(arr) < 2:
        return arr.flatten().tolist()

    tp = arr[0, :].tolist()
    rt = arr[1:, -1].tolist()
    bm = arr[-1:, :-1].flatten()[::-1].tolist()
    lt = arr[1:-1, 0][::-1].tolist()

    return tp + rt + bm + lt + snail(arr[1:-1, 1:-1])


# codewars task best solution
def snail(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + list(reversed(array.pop(-1)))
        res = res + [row.pop(0) for row in array[::-1]]
    return res if not array else res + array[0]


# codewars task best solution
snail = lambda a: list(a[0]) + snail(zip(*a[1:])[::-1]) if a else []


# codewars task best solution
def snail(array):
    return array[0] + snail(list(map(list, [*zip(*array[1::])
                                            ][::-1]))) if array else []


# codewars task best solution
def trans(array):
    #Do an inverse transpose (i.e. rotate left by 90 degrees
    return [[row[-i - 1] for row in array]
            for i in range(len(array[0]))] if len(array) > 0 else array


def snail(array):
    output = []

    while len(array) > 0:

        #Add the 1st row of the array
        output += array[0]
        #Chop off the 1st row and transpose
        array = trans(array[1:])

    return output