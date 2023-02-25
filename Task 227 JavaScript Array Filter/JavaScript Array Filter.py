# my task solution
def get_even_numbers(arr):
    return [i for i in arr if i % 2 == 0]


print(get_even_numbers([2, 4, 5, 6]))
print(get_even_numbers([2, 4, 6, 8]))
print(get_even_numbers([1, 2, 3, 4, 5]))
print(get_even_numbers([1]))
print(get_even_numbers([1]))


# my task solution
def get_even_numbers(arr):

    return list(filter(lambda x: x % 2 == 0, arr))


print(get_even_numbers([2, 4, 5, 6]))


# codewars task best solution
def get_even_numbers(arr):
    return [x for x in arr if x % 2 == 0]


# codewars task best solution
def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))


# codewars task best solution
def get_even_numbers(arr):
    return list(filter(lambda x: not x % 2, arr))


# codewars task best solution
get_even_numbers = lambda arr: [i for i in arr if i % 2 == 0]


# codewars task best solution
def get_even_numbers(arr):
    return [v for v in arr if not v & 1]
