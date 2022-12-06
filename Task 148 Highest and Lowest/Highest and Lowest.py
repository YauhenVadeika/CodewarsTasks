# my task solution
def high_and_low(numbers):

    s = sorted((list(map(int, numbers.split()))))
    return f"{s[-1]} {s[0]}"


print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3 4 5"))


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
