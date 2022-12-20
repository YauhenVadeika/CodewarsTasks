# my task solution
def row_weights(array):

    firstThem = []
    secondThem = []
    [
        secondThem.append(array[i]) if i % 2 else firstThem.append(array[i])
        for i in range(len(array))
    ]
    return sum(firstThem), sum(secondThem)


# print(row_weights([50, 60, 70, 80]))
# print(row_weights([13, 27, 49]))
# print(row_weights([70, 58, 75, 34, 91]))
print(row_weights([100, 51, 50, 100]))


# codewars task best solution
def row_weights(array):
    return sum(array[::2]), sum(array[1::2])


# codewars task best solution
def row_weights(array):
    a = array[::2]
    b = array[1::2]
    return sum(a), sum(b)


# codewars task best solution
def row_weights(array):
    odd = 0
    even = 0
    for i in range(len(array)):
        if i % 2 == 0:
            odd += array[i]
        else:
            even += array[i]
    return odd, even


# codewars task best solution
def row_weights(array):
    evens = sum(i for index, i in enumerate(array) if index % 2 == 0)
    return (evens, sum(array) - evens)


# codewars task best solution
def row_weights(lst):
    return (sum(lst[i] for i in range(0, len(lst), 2)), ) + (sum(
        lst[j] for j in range(1, len(lst), 2)), )


# codewars task best solution
row_weights = lambda arr: (sum(arr[::2]), sum(arr[1::2]))