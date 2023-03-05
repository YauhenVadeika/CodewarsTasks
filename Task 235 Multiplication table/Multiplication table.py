# my task solution
def multiplication_table(size):

    res = []
    a = 1
    while a <= size:
        arr = [i * a for i in range(1, size + 1)]
        res.append(arr)
        a += 1
    return res


print(multiplication_table(3))


# codewars task best solution
def multiplicationTable(size):
    return [[j * i for j in range(1, size + 1)] for i in range(1, size + 1)]


# codewars task best solution
def multiplication_table(size):
    columns = []
    for i in range(1, size + 1):
        rows = []
        for j in range(1, size + 1):
            rows.append(i * j)
        columns.append(rows)

    return columns


# codewars task best solution
def multiplicationTable(size):
    return [[(x + 1) * (y + 1) for y in range(size)] for x in range(size)]


# codewars task best solution
def multiplicationTable(n):
    return [list(range(i, n * i + 1, i)) for i in range(1, n + 1)]


# codewars task best solution
def multiplication_table(size):
    temp_ans = []
    perm_ans = []
    #makes the first list of the table
    first_list = ([size - i for i in range(0, size)])
    first_list.reverse()
    #makes the table's numbers without making it into a nested list
    for i in range(1, size + 1):
        for x in first_list:
            temp_ans.append(i * x)
    #makes the list into a nested list
    for i in range(0, size + 1):
        perm_ans.append(temp_ans[size * (i - 1):size * i])
    #returns the answer
    return perm_ans[1:size + 1]
