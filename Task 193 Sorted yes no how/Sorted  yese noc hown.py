# my task solution
def is_sorted_and_how(arr):

    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"


print(is_sorted_and_how([1, 2]))
print(is_sorted_and_how([15, 7, 3, -8]))
print(is_sorted_and_how([4, 2, 30]))


# codewars task best solution
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr)[::-1]:
        return 'yes, descending'
    else:
        return 'no'


# codewars task best solution
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    elif arr == sorted(arr, reverse=True):
        return 'yes, descending'
    return 'no'


# codewars task best solution
def is_sorted_and_how(arr):
    return 'yes, ascending' if arr == sorted(
        arr) else 'yes, descending' if arr == sorted(arr)[::-1] else 'no'


# codewars task best solution
is_sorted_and_how = lambda a: ['no', 'yes, ascending', 'yes, descending'][
    (sorted(a) == a) + (sorted(a)[::-1] == a) * 2]


# codewars task best solution
def is_sorted_and_how(arr):
    op, txt = ((int.__le__, 'yes, ascending'),
               (int.__ge__, 'yes, descending'))[arr[0] > arr[-1]]
    return all(map(op, arr, arr[1:])) and txt or 'no'