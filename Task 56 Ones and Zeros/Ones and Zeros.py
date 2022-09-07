# my task solution
def binary_array_to_number(arr):
    return sum([(j * (2**abs(i)))for i, j in enumerate(arr, start=-len(arr) + 1)])


print(binary_array_to_number([1, 1, 1, 1]))
print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([1, 0, 1, 1]))


# codewars task best solution
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


# codewars task best solution
def binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)


# codewars task best solution
def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s


# codewars task best solution
def binary_array_to_number(arr):
    return sum(digit * 2**i for i, digit in enumerate(reversed(arr)))