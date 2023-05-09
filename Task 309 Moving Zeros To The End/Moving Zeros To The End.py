"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def move_zeros(lst):

    length = len(lst)
    arr = [i for i in lst if i != 0]
    zeroarr = [0 for j in range(length - len(arr))]
    return arr + zeroarr


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


# codewars task best solution
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i != 0]
    return l + [0] * (len(arr) - len(l))


# codewars task best solution
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


# codewars task best solution
def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)  # Remove the element from the array
            array.append(i)  # Append the element to the end
    return array


# codewars task best solution
def move_zeros(array):
    return [x for x in array if x] + [0] * array.count(0)


# codewars task best solution
def move_zeros(array):
    newarr = []
    zeroarr = []
    for item in array:
        if item != 0 or type(item) == bool:
            newarr.append(item)
        else:
            zeroarr.append(item)

    newarr.extend(zeroarr)
    return (newarr)


# codewars task best solution
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)


# codewars task best solution
def move_zeros(a):
    a.sort(key=lambda v: v == 0)
    return a