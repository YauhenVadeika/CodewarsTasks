# my task solution
def validSolution(board):

    for i in range(len(board)):
        hadd = 0
        vadd = 0
        for j in range(len(board)):

            vadd += board[j][i]

            hadd += board[i][j]

            if board[i][j] < 1 or board[i][j] > 9:
                print(1)
                return False
        if vadd != 45 or hadd != 45:
            print(2)
            print(vadd)
            print(hadd)
            return False
    for i in range(3):
        for j in range(3):
            gadd = 0
            for k in range(3):
                for l in range(3):
                    gadd += board[i * 3 + k][j * 3 + l]
                    if board[i][j] < 1 or board[i][j] > 9:
                        print(3)
                        return False
            if gadd != 45:
                return False
    return True


print(
    validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8],
                   [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3],
                   [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6],
                   [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5],
                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

# codewars task best solution

correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def validSolution(board):
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False

    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return False

    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i * 3:(i + 1) * 3]:
                region += line[j * 3:(j + 1) * 3]

            if sorted(region) != correct:
                return False

    # if everything correct
    return True


# codewars task best solution


# Accessors
def get_row(board, row_index):
    return board[row_index]


def get_col(board, col_index):
    return [row[col_index] for row in board]


def get_subgrid(board, base_x, base_y):
    # Returns elements (array) in a 3x3 subgrid
    # base_x,base_y are the x,y coordinates of the top-left element in the 3x3 subgrid
    result = []
    for x in range(0, 3):
        for y in range(0, 3):
            result.append(board[base_x + x][base_y + y])
    return result


class InvalidSudokuSet(Exception):
    pass


def validate_9(arr, identifier="Group"):
    # Validates any 9 elements
    if len(arr) != 9:
        raise InvalidSudokuSet("{} has length {} (not 9): {}".format(
            identifier, len(arr), arr))

    for number in range(1, 10):
        if number not in arr:
            raise InvalidSudokuSet("{} is missing '{}': {}".format(
                identifier, number, arr))


def validate_dimensions(board):
    if len(board) != 9:
        raise InvalidSudokuSet("Board contains {} rows:\n{}".format(
            len(board), board))
    for row in board:
        if len(row) != 9:
            raise InvalidSudokuSet(
                "Row does not have 9 columns:\n{}".format(board))


def validate_rows(board):
    for index in range(0, 9):
        validate_9(get_row(board, index), "Row")


def validate_columns(board):
    for index in range(0, 9):
        validate_9(get_col(board, index), "Column")


def validate_subgrids(board):
    for x in range(0, 3):
        for y in range(0, 3):
            subgrid = get_subgrid(board, x * 3, y * 3)
            validate_9(subgrid, identifier="3x3 Subgrid")


def validSolution(board):
    try:
        validate_dimensions(board)
        validate_rows(board)
        validate_columns(board)
        validate_subgrids(board)

    except InvalidSudokuSet as e:
        print("Invalid board:\n{}\n".format(board))
        print(e)
        return False

    print("Valid board:\n{}".format(board))
    return True


# codewars task best solution

import numpy as np
from itertools import chain

nums = set(range(1, 10))


def validSolution(board):
    a = np.array(board)
    r = range(0, 9, 3)
    return all(
        set(v.flatten()) == nums
        for v in chain(a, a.T, (a[i:i + 3, j:j + 3] for i in r for j in r)))


# codewars task best solution


def validSolution(board):
    good = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in board:
        if sorted(i) == good: continue
        else: return False
    for i in zip(*board):
        if sorted(i) == good: continue
        else: return False
    for x in (0, 3, 6):
        for y in (0, 3, 6):
            subgrid = board[y][x:x + 3] + board[y + 1][x:x +
                                                       3] + board[y + 2][x:x +
                                                                         3]
            if sorted(subgrid) == good:
                continue
            else:
                return False
    return True
