# my task solution
import math


def stringFactors(list_factors):
    output_string = ""
    distinct_factors = set(list_factors)
    for factor in sorted(distinct_factors):
        if list_factors.count(factor) == 1:
            output_string = output_string + "(" + str(factor) + ")"
        else:
            output_string = output_string + "(" + str(factor) + "**" + str(
                list_factors.count(factor)) + ")"
    return output_string


def prime_factors(num):
    working_num = num
    factors = []
    for i in range(2, working_num + 1):
        while working_num % i == 0:
            factors.append(i)
            working_num /= i
        if working_num == 1:
            return stringFactors(factors)
    return stringFactors(factors)


print(prime_factors(7775460))


# codewars task best solution
def primeFactors(n):
    i, j, p = 2, 0, []
    while n > 1:
        while n % i == 0:
            n, j = n / i, j + 1
        if j > 0: p.append([i, j])
        i, j = i + 1, 0
    return ''.join('(%d' % q[0] + ('**%d' % q[1]) * (q[1] > 1) + ')'
                   for q in p)


# codewars task best solution
def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n % i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0:
            pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1

    return r


# codewars task best solution
def primeFactors(n):
    result = ''
    fac = 2
    while fac <= n:
        count = 0
        while n % fac == 0:
            n /= fac
            count += 1
        if count:
            result += '(%d%s)' % (fac, '**%d' % count if count > 1 else '')
        fac += 1
    return result
