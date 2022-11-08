# my task solution
def sum_digits(number):
    return sum([int(i) for i in list(str(abs(number)))])


print(sum_digits(10))
print(sum_digits(99))
print(sum_digits(-32))


# codewars task best solution
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))


# codewars task best solution
def sumDigits(number):
    number = abs(number)
    return_number = 0

    while number > 0:
        return_number += number % 10
        number = int(number / 10)

    return return_number