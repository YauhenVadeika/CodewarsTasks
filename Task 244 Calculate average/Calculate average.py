# my task solution
def find_average(numbers):
    return sum(numbers) / len(numbers)


print(find_average([1, 2, 3]))


# codewars task best solution
def find_average(array):
    return sum(array) / len(array) if array else 0


# codewars task best solution
def find_average(numbers):
    return sum(numbers) / len(numbers)


# codewars task best solution
def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0


# codewars task best solution
from statistics import mean as find_average


# codewars task best solution
def find_average(array):
    if not array:
        return 0

    class SafeFloat(object):

        def __init__(self, val):
            super(SafeFloat, self).__init__()
            self.val = val

        def __eq__(self, float_val):
            # let me fix your comparisons..
            def isclose(a, b):
                return abs(a - b) < 0.00000001

            return isclose(self.val, float_val)

        def __str__(self):
            return str(self.val)

    from numpy import mean
    return SafeFloat(mean(array))
