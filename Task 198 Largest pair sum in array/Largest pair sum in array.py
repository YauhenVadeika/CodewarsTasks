# my task solution
def largest_pair_sum(numbers):
    return sum((sorted(numbers))[-2:])


print(largest_pair_sum([10, 14, 2, 23, 19]))
print(largest_pair_sum([-100, -29, -24, -19, 19]))
print(largest_pair_sum([1, 2, 3, 4, 6, -1, 2]))
print(largest_pair_sum([-10, -8, -16, -18, -19]))

# codewars task best solution
from heapq import nlargest


def largest_pair_sum(a):
    return sum(nlargest(2, a))


# codewars task best solution
def largest_pair_sum(numbers):
    # your code here
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 + max2


# codewars task best solution
def largest_pair_sum(a):
    return a.pop(a.index(max(a))) + a.pop(a.index(max(a)))


# codewars task best solution
def largest_pair_sum(numbers):
    return sorted(numbers)[-2] + max(numbers)


# codewars task best solution
def largest_pair_sum(numbers):
    from heapq import nlargest
    return sum(nlargest(2, numbers))


# codewars task best solution
def largest_pair_sum(num):
    return num.pop(num.index(max(num))) + max(num)