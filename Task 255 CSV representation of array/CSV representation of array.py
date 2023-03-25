# my task solution
def to_csv_text(array):
    return '\n'.join([','.join(map(str, i)) for i in array])


print(
    to_csv_text([[0, 1, 2, 3, 45], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24],
                 [30, 31, 32, 33, 34]]))


# codewars task best solution
def toCsvText(array):
    return '\n'.join(','.join(map(str, line)) for line in array)


# codewars task best solution
def toCsvText(array):
    return '\n'.join(','.join(str(n) for n in lst) for lst in array)


# codewars task best solution
def toCsvText(array):
    return (str(array).replace('],',
                               '\n').replace('[',
                                             '').replace(']',
                                                         '').replace(' ', ''))


# codewars task best solution
def toCsvText(array):
    rs = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = str(array[i][j])
        rs.append(','.join(array[i]))
    return '\n'.join(rs)


# codewars task best solution
def toCsvText(array):
    return '\n'.join(','.join(map(str, row)) for row in array)