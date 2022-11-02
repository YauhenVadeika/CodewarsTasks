# my task solution
def square_sum(numbers):

    return sum([i**2 for i in numbers])


print(square_sum([1, 2, 2]))
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))


# codewars task best solution
def square_sum(numbers):
    return sum(x**2 for x in numbers)


# codewars task best solution
def square_sum(numbers):
    return sum(map(lambda x: x**2, numbers))


# codewars task best solution
def square_sum(numbers):
    res = 0
    for num in numbers:
        res = res + num * num
    return res