# my task solution
def array(string):
    return " ".join((string.split(",")[1:-1])) or None


print(array('1,2,3'))
print(array('1,2,3,4'))
print(array(''))
print(array('1'))
print(array('1,2'))


# codewars task best solution
def array(s):
    r = ' '.join(s.split(',')[1:-1])
    return r if r else None


# codewars task best solution
def array(string):
    res = ' '.join(string.split(',')[1:-1])
    return res if len(res) > 0 else None


# codewars task best solution
def array(s):
    return ' '.join(s.split(',')[1:-1]) or None


# codewars task best solution
def array(_s):
    arr = _s.split(',')
    if len(arr) == 0:
        return None
    else:
        del (arr[0])
    if len(arr) == 0:
        return None
    else:
        del (arr[-1])
    s = ' '.join(arr)
    return None if s == '' else s