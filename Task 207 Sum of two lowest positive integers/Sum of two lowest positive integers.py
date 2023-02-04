# my task solution
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))


# codewars task best solution
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


# codewars task best solution
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]


# codewars task best solution
def sum_two_smallest_numbers(numbers):
    smallest1 = None
    smallest2 = None
    for n in numbers:
        if not smallest1 or n < smallest1:
            smallest2 = smallest1
            smallest1 = n
        elif not smallest2 or n < smallest2:
            smallest2 = n
    return smallest1 + smallest2


# codewars task best solution
def sum_two_smallest_numbers(numbers):
    first_min = min(numbers)
    numbers.remove(first_min)
    second_min = min(numbers)
    return first_min + second_min


# codewars task best solution
from heapq import nsmallest


def sum_two_smallest_numbers(numbers):
    return sum(nsmallest(2, numbers))
