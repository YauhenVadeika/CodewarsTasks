# my task solution
def name_shuffler(str):
    return ' '.join([i for i in ((str.split())[1], (str.split())[0])])


print(name_shuffler("john McClane"))
print(name_shuffler('Mary jeggins'))
print(name_shuffler('tom jerry'))


# codewars task best solution
def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


# codewars task best solution
def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first


# codewars task best solution
def name_shuffler(s):
    return ' '.join(reversed(s.split()))


# codewars task best solution
name_shuffler = lambda s: ' '.join(reversed(s.split()))