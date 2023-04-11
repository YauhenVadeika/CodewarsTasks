"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def high_and_low(numbers):

    arr = (sorted(map(int, numbers.split()), reverse=True))
    return f"{str(arr[0])} {str(arr[-1])}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


# codewars task best solution
def high_and_low(numbers):  #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))


# codewars task best solution
def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])


# codewars task best solution
def high_and_low(numbers):
    numbers = [int(c) for c in numbers.split(' ')]
    return f"{max(numbers)} {min(numbers)}"


# codewars task best solution
def high_and_low(numbers):
    return " ".join(x(numbers.split(), key=int) for x in (max, min))


# codewars task best solution
def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))