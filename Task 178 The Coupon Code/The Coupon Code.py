# my task solution
import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        return (datetime.datetime.strptime(current_date, '%B %d, %Y') <=
                datetime.datetime.strptime(expiration_date, '%B %d, %Y'))
    return False


print(check_coupon('123', '123', 'September 5, 2014',
                   'October 1, 2014'))  #True
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))  # False
print(check_coupon('123a', '123', 'September 5, 2014',
                   'October 1, 2014'))  #False
print(check_coupon('123', '123', 'July 9, 1988', 'June 16, 1997'))  # True
print(check_coupon('123', '123', 'September 5, 2014',
                   'September 25, 2014'))  # True

# codewars task best solution
import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    strptime = datetime.datetime.strptime
    format = "%B %d, %Y"
    return strptime(current_date, format) <= strptime(expiration_date, format) and\
                             entered_code is correct_code


# codewars task best solution
from datetime import datetime


def check_coupon(ent, corr, curr_d, exp_d):
    d1 = datetime.strptime(curr_d, '%B %d, %Y')
    d2 = datetime.strptime(exp_d, '%B %d, %Y')
    return ent is corr and d1 <= d2


# codewars task best solution
from dateutil import parser


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    return entered_code == correct_code and parser.parse(
        current_date) <= parser.parse(expiration_date) if type(
            correct_code) == str else False


# codewars task best solution
from datetime import datetime as dt


def check_coupon(entered, correct, current, expiration):
    date = lambda stg: dt.strptime(stg, "%B %d, %Y")
    return entered == correct and type(entered) == type(
        correct) and date(current) <= date(expiration)
