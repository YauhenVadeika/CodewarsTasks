# my task solution
def two_decimal_places(n):
    return round(n, 2)


print(two_decimal_places(5.5589))
print(two_decimal_places(4.659725356))


# codewars task best solution
def two_decimal_places(n):
    return round(n * 100) / 100


# codewars task best solution
from decimal import Decimal, ROUND_HALF_UP


def two_decimal_places(n):
    dn = Decimal(str(n)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    return float(dn)


# codewars task best solution
def two_decimal_places(n):
    return float("{0:.2f}".format(n))


# codewars task best solution
def two_decimal_places(n):
    return float("%.2f" % n)


# codewars task best solution
def two_decimal_places(n):
    """
    a nightmare in a small package
    """

    # Convert to a string
    x = str(n)

    # find the decimal
    ptIndx = x.find(".")

    # grab the deciding digit
    roundingDigit = x[ptIndx + 3]

    # create the return string
    o = x[0:ptIndx + 3]

    # return if not rounding up
    if int(roundingDigit) <= 4:
        return float(o)
    else:
        # round the result of "rounding", since if you don't you get some ###.###9999999764235761923765 garbage
        return round(float(o) + (-0.01 if x[0] == "-" else 0.01), 2)

    #I can't wait to see more appropriate solutions.


# codewars task best solution
two_decimal_places = lambda n: round(n, 2)
