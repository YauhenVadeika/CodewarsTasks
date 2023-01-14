# my task solution
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    num = 0
    for i in range(len(matrix)):
        num += (1 if i % 2 == 0 else -1) * matrix[0][i] * determinant(
            [j[:i] + j[i + 1:] for j in matrix[1:]])
    return num


print(determinant([[4, 6], [3, 8]]))
print(determinant([[2, 4, 2], [3, 1, 1], [1, 2, 0]]))

# codewars task best solution
import numpy as np


def determinant(a):
    return round(np.linalg.det(np.matrix(a)))


# codewars task best solution
import numpy as np


def determinant(matrix):
    return round(np.linalg.det(matrix))


# codewars task best solution
def determinant(matrix):
    #your code here
    result = 0
    l = len(matrix)

    #base case when length of matrix is 1
    if l == 1:
        return matrix[0][0]

    #base case when length of matrix is 2
    if l == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    #for length of matrix > 2
    for j in range(0, l):
        # create a sub matrix to find the determinant
        if l != 2:
            sub_matrix = []
            sub_matrix = [(row[0:j] + row[j + 1:]) for row in matrix[1:]]
        result = result + (-1)**j * matrix[0][j] * determinant(sub_matrix)
    return result


# codewars task best solution
def sub_determinant(matrix, i):
    sub_matrix = []
    for j in range(1, len(matrix)):
        sub_matrix.append(matrix[j][:i] + matrix[j][i + 1:])
    return sub_matrix


def determinant(matrix):
    if len(matrix) == 0:
        return 0
    elif len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        sum = 0
        for i in range(0, len(matrix)):
            if 1 == i & 1:
                sum = sum - matrix[0][i] * determinant(
                    sub_determinant(matrix, i))
            else:
                sum = sum + matrix[0][i] * determinant(
                    sub_determinant(matrix, i))
        return sum


# codewars task best solution
import copy


def create_lesser_matrix(matrix, j):
    matrix_copy = copy.deepcopy(matrix)
    del matrix_copy[0]

    for row in matrix_copy:
        del row[j]
    return matrix_copy


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    det = 0
    for i in range(len(matrix)):
        det += (-1)**i * matrix[0][i] * determinant(
            create_lesser_matrix(matrix, i))
    return det