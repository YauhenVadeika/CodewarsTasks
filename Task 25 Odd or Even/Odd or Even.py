# my task solution
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


print(odd_or_even([0]))
print(odd_or_even([0, 1, 4]))
print(odd_or_even([0, -1, -5]))

# codewars task best solution
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


# codewars task best solution
def oddOrEven(arr):
    """determine whether a given list of numbers is odd or even"""
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"
