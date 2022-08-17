# my task solution
def filter_list(l):
    lst = []
    for i in l:
        if type(i) == int:
            lst.append(i)
    return lst


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'а', 'б', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))

# codewars task best solution


def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]


# codewars task best solution
def filter_list(l):
    'return a new list with the strings filtered out'
    return [x for x in l if type(x) is not str]


# codewars task best solution
def filter_list(l):
    'return a new list with the strings filtered out'
    return [e for e in l if isinstance(e, int)]
