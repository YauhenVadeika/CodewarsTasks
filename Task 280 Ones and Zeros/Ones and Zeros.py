"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def binary_array_to_number(arr):
    return sum(
        [val * (2**(abs(ind))) for ind, val in enumerate(arr, -len(arr) + 1)])


print(binary_array_to_number([1, 1, 0, 1]))
print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([1, 1, 1, 1]))
print(binary_array_to_number([0, 0, 1, 0]))


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


# codewars task best solution
def binary_array_to_number(arr):
    return sum(2**i for i, n in enumerate(arr[::-1]) if n)


# codewars task best solution
def binary_array_to_number(arr):
    append_bit = lambda n, b: n << 1 | b
    return reduce(append_bit, arr)