# my task solution
def multi_table(number):
    res = ''
    for i in range(1, 11):
        res += f'{i} * {number} = {number * i}\n'
    return res[:-1]


print(multi_table(5))


# codewars task best solution
def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


# codewars task best solution
def multi_table(number):
    table = [
        "{0} * {1} = {2}".format(i, number, i * number) for i in range(1, 11)
    ]
    return '\n'.join(table)


# codewars task best solution
def multi_table(n):
    return '\n'.join(f'{i} * {n} = {i*n}' for i in range(1, 11))


# codewars task best solution
def multi_table(number):
    st = str()
    for x in range(1, 11):
        z = number * x
        st += '{} * {} = {}\n'.format(x, number, z)
    sti = st.strip('\n')
    return sti


# codewars task best solution
def multi_table(n):
    return "\n".join([f"{i} * {n} = {i * n}" for i in range(1, 11)])


# codewars task best solution
multi_table = lambda n: '\n'.join('%i * %i = %i' % (i, n, i * n)
                                  for i in range(1, 11))
