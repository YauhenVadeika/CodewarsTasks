# my task solution
def find_longest(arr):

    return ([i for i in arr if len(str(i)) == len(str(max(arr)))])[0]


print(find_longest([1, 10, 100]))
print(find_longest([8, 500, 900]))


# codewars task best solution
def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))


# codewars task best solution
def find_longest(arr):
    arr.sort(reverse=True)
    return arr[0]


# codewars task best solution
def find_longest(arr):
    #your code here
    max_lenght = 0
    max_index = 0
    for cur_num in arr:
        lenght = len(str(cur_num))
        if lenght > max_lenght:
            max_lenght = lenght
            max_index = arr.index(cur_num)
    return arr[max_index]


# codewars task best solution
def find_longest(arr):
    e = [len(str(i)) for i in arr]
    return arr[e.index(max(e))]


# codewars task best solution
from math import log10


def find_longest(arr):
    return max(arr, key=lambda n: int(log10(n)))
