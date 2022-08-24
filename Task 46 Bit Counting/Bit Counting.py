# my task solution
def count_bits(n):
    return bin(n).count('1')


print(count_bits(1234))
print(count_bits(0))
print(count_bits(4))


# codewars task best solution
def countBits(n):
    return bin(n).count("1")


# codewars task best solution
def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total


# codewars task best solution
def countBits(n):
    return bin(n)[2:].count('1')


# codewars task best solution
def countBits(n):
    """ count_bits == PEP8, forced camelCase by CodeWars """
    return '{:b}'.format(n).count('1')
