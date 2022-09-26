# my task solution
def gimme(input_array):
    return ([input_array.index(i) for i in input_array if i < max(input_array) and i > min(input_array)][0])


print(gimme([2, 3, 1]))
print(gimme([5, 10, 14]))


# my task solution
def gimme(input_array):
    for i in input_array:
        if i < max(input_array) and i > min(input_array):
            return input_array.index(i)


print(gimme([2, 3, 1]))
print(gimme([5, 10, 14]))


# codewars task best solution
def gimme(inputArray):
    # Implement this function
    return inputArray.index(sorted(inputArray)[1])


# codewars task best solution
def gimme(lst):
    return lst.index(sorted(lst)[len(lst)//2])


# codewars task best solution
def gimme(arr):
    arr1 = sorted(arr)
    middle = arr1[1]
    return arr.index(middle) 