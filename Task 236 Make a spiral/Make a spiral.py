# my task solution
def spiralize(size):

    matrix = list(
        map(
            lambda x: list(
                map(lambda y: 1
                    if (int(size + 1) / 2) % 2 == 1 else 0, range(0, size))),
            range(0, size)))
    spiral = 1
    for i in range(0, int(size / 2)):
        for u in range(0, size - i * 2):
            matrix[i][u + i] = spiral
            matrix[u + i][i] = spiral
            matrix[size - i - 1][u + i] = spiral
            matrix[u + i][size - i - 1] = spiral

            if size % 4 == 0:
                if i != int(size / 2) - 1:
                    matrix[i + 1][i] = 1 - spiral
            else:
                matrix[i + 1][i] = 1 - spiral
        spiral = 1 - spiral
    return matrix


print(spiralize(8))


# codewars task best solution
def spiralize(size):

    def on_board(x, y):
        return 0 <= x < size and 0 <= y < size

    def is_one(x, y):
        return on_board(x, y) and spiral[y][x] == 1

    def can_move():
        return on_board(
            x + dx, y + dy) and not (is_one(x + 2 * dx, y + 2 * dy) or is_one(
                x + dx - dy, y + dy + dx) or is_one(x + dx + dy, y + dy - dx))

    spiral = [[0 for x in range(size)] for y in range(size)]
    x, y = -1, 0
    dx, dy = 1, 0
    turns = 0

    while (turns < 2):
        if can_move():
            x += dx
            y += dy
            spiral[y][x] = 1
            turns = 0
        else:
            dx, dy = -dy, dx
            turns += 1

    return spiral


# codewars task best solution
def spiralize(size):
    # Make a snake
    spiral = [[1 - min(i, j, size - max(i, j) - 1) % 2 for j in xrange(size)]
              for i in xrange(size)]
    for i in xrange(size / 2 - (size % 4 == 0)):
        spiral[i + 1][i] = 1 - spiral[i + 1][i]
    return spiral


# codewars task best solution
import numpy as np


def spiralize(size):
    if size == 0:
        return []
    if size == 1:
        return [[1]]
    if size == 2:
        return [[1, 1], [0, 1]]
    sp = np.zeros((size, size))
    sp[0, :] = 1
    sp[:, -1] = 1
    sp[-1, :] = 1
    sp[2:, :-2] = np.array(spiralize(size - 2))[::-1, ::-1]
    return sp.tolist()


# codewars task best solution
def layer(spiral):
    """Wraps one extra layer around an existing spiral."""
    val = spiral[0][0] ^ 1
    top = (2 + len(spiral[0])) * [val]
    first = [val ^ 1] + spiral[0] + [val]
    other = [[val] + row + [val] for row in spiral[1:]]
    return [top, first] + other + [top]


def spiralize(size):
    """The snake is recursive."""
    a = [[1]]
    b = [[1, 1], [0, 1]]
    c = [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
    d = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]

    if size < 5:
        return [d, a, b, c][size % 4] if size else []

    return layer(layer(spiralize(size - 4)))


# codewars task best solution
def spiralize(size):
    canvas = [[0] * size for i in range(size)]
    length = size
    pos = [0, 0]
    dir = "E"
    for i in range(size):
        move = get_move(dir)
        for j in range(length):
            canvas[pos[0] + move[0] * j][pos[1] + move[1] * j] = 1
        pos[0] += move[0] * (length - 1)
        pos[1] += move[1] * (length - 1)
        if i != 0 and i % 2 == 0:
            length -= 2
        dir = turn_right(dir)
    return canvas


def get_move(dir):
    if dir == "E":
        return (0, 1)
    elif dir == "S":
        return (1, 0)
    elif dir == "W":
        return (0, -1)
    else:
        return (-1, 0)


def turn_right(dir):
    if dir == "E":
        return "S"
    elif dir == "S":
        return "W"
    elif dir == "W":
        return "N"
    else:
        return "E"