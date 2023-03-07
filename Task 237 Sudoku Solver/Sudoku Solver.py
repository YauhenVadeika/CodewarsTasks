# my task solution
def sudoku(puzzle):

    def vaild(puzzle):
        for m in range(9):
            if puzzle[m][j] == puzzle[i][j] and m != i:
                return False
        for n in range(9):
            if puzzle[i][n] == puzzle[i][j] and n != j:
                return False
        for m in range(3):
            for n in range(3):
                if puzzle[int(i / 3) * 3 + m][
                        int(j / 3) * 3 +
                        n] == puzzle[i][j] and m != i and n != j and int(
                            i / 3) * 3 + m != i and int(j / 3) * 3 + n != j:
                    return False
        return True

    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for d in range(1, 10):
                    puzzle[i][j] = d
                    if vaild(puzzle):
                        if sudoku(puzzle):
                            return puzzle
                        else:
                            puzzle[i][j] = 0
                    else:
                        puzzle[i][j] = 0
                return False
    return puzzle


print(
    sudoku([[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]))


# codewars task best solution
def sudoku(P):

    for row, col in [(r, c) for r in range(9) for c in range(9)
                     if not P[r][c]]:

        rr, cc = (row // 3) * 3, (col // 3) * 3

        use = {1, 2, 3, 4, 5, 6, 7, 8, 9
               } - ({P[row][c]
                     for c in range(9)} | {P[r][col]
                                           for r in range(9)}
                    | {P[rr + r][cc + c]
                       for r in range(3) for c in range(3)})

        if len(use) == 1:
            P[row][col] = use.pop()
            return sudoku(P)
    return P


# codewars task best solution
def update(spots, row, col, l):
    if (row, col) in spots:
        spots[(row, col)] = spots[(row, col)].difference(set(l))


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    spots = {}
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                spots[(row, col)] = set(range(1, 10))

    while len(spots) > 0:
        for (row, col) in spots:
            r = int(row / 3) * 3
            c = int(col / 3) * 3
            square = puzzle[r][c:c + 3] + puzzle[r + 1][c:c +
                                                        3] + puzzle[r +
                                                                    2][c:c + 3]
            update(spots, row, col, puzzle[row])
            update(spots, row, col, zip(*puzzle)[col])
            update(spots, row, col, square)

        for (row, col) in [(r, c) for (r, c) in spots]:
            if len(spots[(row, col)]) == 1:
                puzzle[row][col] = spots[(row, col)].pop()
                del spots[(row, col)]
    return puzzle


# codewars task best solution
def sudoku(puzzle):

    class Point:

        def __init__(self, grid, x, y):
            self.x = x
            self.y = y
            self.value = grid[x][y]
            self.grid = grid
            self.grid3 = [
                item for sublist in [
                    i[(y // 3) * 3:(y // 3 + 1) * 3]
                    for i in grid[(x // 3) * 3:(x // 3 + 1) * 3]
                ] for item in sublist
            ]
            self.hline = grid[x]
            self.vline = [row[y] for row in grid]

    islist = 1
    while islist > 0:
        islist = 0
        for x in range(0, 9):
            for y in range(0, 9):
                p = Point(puzzle, x, y)
                if p.value == 0 or type(p.value) == list:
                    islist = 1
                    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    for i in p.grid3:
                        if i in possible:
                            possible.remove(i)
                    for i in p.hline:
                        if i in possible:
                            possible.remove(i)
                    for i in p.vline:
                        if i in possible:
                            possible.remove(i)
                    if len(possible) == 1:
                        puzzle[x][y] = possible[0]
                        print(possible)
                    else:
                        puzzle[x][y] = possible
                        print(possible)

    print(puzzle)

    return puzzle


# codewars task best solution
def check_num(c, puzzle):
    c_r = [
        puzzle[i][c[1]] for i in range(len(puzzle)) if puzzle[i][c[1]] != 0
    ] + [n for n in puzzle[c[0]] if n != 0]
    box = [
        n for x in c for n in ((0, 3), (3, 6), (6, 9))
        if x in range(n[0], n[1])
    ]
    boxes = [
        puzzle[i][j] for i in range(box[0][0], box[0][1])
        for j in range(box[1][0], box[1][1]) if puzzle[i][j] != 0
    ]
    result = [n for n in range(1, 10) if n not in set(c_r + boxes)]
    return result[0] if len(result) == 1 else 0


def sudoku(puzzle, z=False):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                puzzle[i][j] = check_num((i, j), puzzle)
                if z == False and puzzle[i][j] == 0:
                    z = True
    return puzzle if z is False else sudoku(puzzle, False)


# codewars task best solution
import numpy as np
import copy


def sudoku(m):
    """return the solved puzzle as a 2d array of 9 x 9"""
    r = np.zeros((10, 10), dtype=np.int)
    c = np.zeros((10, 10), dtype=np.int)
    cell = np.zeros((10, 10, 10), dtype=np.int)
    cnt = 0
    gridx, gridy = [], []

    for i in range(9):
        for j in range(9):
            v = m[i][j]
            if v == 0:
                cnt += 1
                gridx.append(i)
                gridy.append(j)
            else:
                r[i][v] = c[j][v] = cell[i // 3][j // 3][v] = v

    ans = None

    def dfs(l):
        global fl
        if l >= cnt:
            nonlocal ans
            ans = copy.deepcopy(m)
            return
        i, j = gridx[l], gridy[l]

        for v in range(1, 10):
            if r[i][v] > 0 or c[j][v] > 0 or cell[i // 3][j // 3][v] > 0:
                continue
            else:
                r[i][v] = c[j][v] = cell[i // 3][j // 3][v] = m[i][j] = v
                dfs(l + 1)
                r[i][v] = c[j][v] = cell[i // 3][j // 3][v] = m[i][j] = 0

    dfs(0)
    return ans
