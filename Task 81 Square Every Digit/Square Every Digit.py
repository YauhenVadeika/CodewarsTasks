# my task solution
def square_digits(num):
    return int(''.join([str(int(i) * int(i)) for i in str(num)]))


print(square_digits(9119))
print(square_digits(0))


# codewars task best solution
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)


# codewars task best solution
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))


# codewars task best solution
def square_digits(num):
    return int(''.join([str(n * n) for n in map(int, str(num))]))