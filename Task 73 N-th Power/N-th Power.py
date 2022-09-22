def index(array, n):
    return array[n]**n if n < len(array) else -1


print(index([1, 2, 3, 4], 2))


# codewars task best solution
def index(array, n):
    try:
        return array[n]**n
    except:
        return -1


# codewars task best solution
def index(array, n):
    if n < len(array):
        return (array[n])**n
    else:
        return -1