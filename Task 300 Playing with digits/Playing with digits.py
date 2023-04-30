"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def dig_pow(n, p):

    res = (sum([int(value)**num for num, value in enumerate(str(n), p)]))
    if res % n == 0:
        return int(res / n)
    return -1


print(dig_pow(46288, 3))
print(dig_pow(89, 1))


# codewars task best solution
def dig_pow(n, p):
    s = 0
    for i, c in enumerate(str(n)):
        s += pow(int(c), p + i)
    return s / n if s % n == 0 else -1


# codewars task best solution
def dig_pow(n, p):
    k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n)
    return -1 if fail else k


# codewars task best solution
def dig_pow(n, p):
    t = sum(int(d)**(p + i) for i, d in enumerate(str(n)))
    return t // n if t % n == 0 else -1


# codewars task best solution
def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += int(c)**p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1


# codewars task best solution
def dig_pow(n, p):
    # your code
    n_list = [int(i) for i in str(n)]
    n_sum = 0
    p_i = p
    for n_i in n_list:
        n_sum = n_sum + n_i**p_i
        p_i = p_i + 1
    if n_sum % n == 0:
        return n_sum / n
    else:
        return -1


# codewars task best solution
def dig_pow(n, p):
    s = sum(int(d)**(p + i) for i, d in enumerate(str(n)))
    return s / n if s % n == 0 else -1


# codewars task best solution
def dig_pow(n, p):
    digit_power = sum(int(x)**pw for pw, x in enumerate(str(n), p))
    if digit_power % n == 0:
        return digit_power / n
    return -1


# codewars task best solution
dig_pow = lambda n, p: [
    -1 if sum([(int(str(n)[i]))**(p + i)
               for i in range(len(str(n)))]) / n != sum([
                   (int(str(n)[i]))**(p + i) for i in range(len(str(n)))
               ]) // n else sum([(int(str(n)[i]))**(p + i)
                                 for i in range(len(str(n)))]) // n
][0]
