# my task solution
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))


print(sequence_sum(2, 2, 2))
print(sequence_sum(2, 6, 2))
print(sequence_sum(1, 5, 1))
print(sequence_sum(1, 5, 3))
print(sequence_sum(0, 15, 3))
print(sequence_sum(15, 1, 3))


# codewars task best solution
def sequence_sum(start, end, step):
    return sum(range(start, end + 1, step))


# codewars task best solution
def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number + 1, step))


# codewars task best solution
def sequence_sum(b, e, s):
    k = (e - b) // s
    return (1 + k) * (b + s * k / 2) if b <= e else 0


# codewars task best solution
sequence_sum = lambda b, e, s: sum(range(b, e + 1, s))