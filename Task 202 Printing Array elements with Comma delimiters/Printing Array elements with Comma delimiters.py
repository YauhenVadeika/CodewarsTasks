# my task solution
def print_array(arr):
    return ",".join(list(map(str, (arr))))


print(print_array([2, 4, 5, 2]))
print(print_array([True, False, False]))


# codewars task best solution
def print_array(arr):
    return ','.join(map(str, arr))


# codewars task best solution
def print_array(arr):
    return ','.join(str(a) for a in arr)


# codewars task best solution
print_array = lambda a: ','.join(map(str, a))


# codewars task best solution
def print_array(arr):
    result = ''
    for i in range(0, len(arr)):
        if i == len(arr):
            result += str(arr[i])
        else:
            result += str(arr[i]) + ','
    if result.endswith(","):
        return result[:-1]
    return result


# codewars task best solution
def print_array(arr):
    result = []
    for ar in arr:
        if ar is list:
            result.append(print_array(ar))
        else:
            result.append(str(ar))
    return ','.join(result)