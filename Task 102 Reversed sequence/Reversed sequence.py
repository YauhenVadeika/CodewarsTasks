# my task solution
def reverse_seq(n):
    return [i for i in range(n, 0, -1)]


print(reverse_seq(5))


# codewars task best solution
def reverseseq(n):
    return list(range(n, 0, -1))


# codewars task best solution
def reverseseq(n):
    return range(n, 0, -1)


# codewars task best solution
def reverse_seq(a):
    if a > 0:
        return (list(range(a, 0, -1)))
    else:
        return ("pick a positive number")
