# my task solution
def find_smallest_int(arr):
    return min(sorted(arr))


print(find_smallest_int([34, 15, 88, 2]))
print(find_smallest_int([0, 1 - 2**64, 2**64]))


# codewars task best solution
def findSmallestInt(arr):
    return min(arr)


# codewars task best solution
def findSmallestInt(arr):
    #sort array
    arr.sort()
    return arr[0]


# codewars task best solution
def findSmallestInt(arr):
    smallest = []
    for i in range(0, len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
    return smallest