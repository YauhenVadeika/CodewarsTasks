# my task solution
def find_needle(haystack):
    if 'needle' in haystack:
        return f"found the needle at position {haystack.index('needle')}"


print(
    find_needle([
        '3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False
    ]))


# codewars task best solution
def find_needle(haystack):
    return 'found the needle at position %d' % haystack.index('needle')


    # codewars task best solution
def find_needle(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))


# codewars task best solution
def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == 'needle':
            return 'found the needle at position %d' % i


    # codewars task best solution
def find_needle(haystack):
    # your code here
    if 'needle' in haystack:
        return 'found the needle at position %d' % haystack.index('needle')
    # codewars task best solution


find_needle = lambda haystack: "found the needle at position {}".format(
    haystack.index("needle"))
