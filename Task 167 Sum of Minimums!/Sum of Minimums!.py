# my task solution
def sum_of_minimums(numbers):
    return sum([min(i) for i in numbers])


print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]))
print(
    sum_of_minimums([[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3],
                     [9, 8, 6, 7]]))


# codewars task best solution
def sum_of_minimums(numbers):
    return sum(map(min, numbers))


# codewars task best solution
def sum_of_minimums(numbers):
    return sum([min(rows) for rows in numbers])


# codewars task best solution
def sum_of_minimums(numbers):
    total = 0
    for nums in numbers:
        total += min(nums)
    return total


# codewars task best solution
sum_of_minimums = lambda l: sum(min(e) for e in l)
