# my task solution
def powers_of_two(n):
    return [2**i for i in list(range(n+1))]


print(powers_of_two(0))
print(powers_of_two(1))
print(powers_of_two(2))
print(powers_of_two(4))

# codewars task best solution
def powers_of_two(n):
    return [2**x for x in range(n+1)]


# codewars task best solution
def powers_of_two(n):
    a = []
    for i in range(0, n + 1):
        a.append(2 ** i)    
    return a


# codewars task best solution
def powers_of_two(n):
    return [1<<x for x in range(n + 1)]