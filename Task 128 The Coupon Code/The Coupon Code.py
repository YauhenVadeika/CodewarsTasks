# my task solution
def check_coupon(entered_code, correct_code, current_date, expiration_date):

    # Array Month
    month = "January", "February", "March", "April", "May", "June", "July",\
        "August", "September", "October", "November", "December"

    # Day
    curentDay = int((current_date.split(',')[0]).split(' ')[1])
    expirationDay = int((expiration_date.split(',')[0]).split(' ')[1])

    # Month
    curentMonth = month.index((current_date.split(',')[0]).split(' ')[0])
    expirationMonth = month.index(
        (expiration_date.split(',')[0]).split(' ')[0])

    # Year
    curentYear = int(current_date.split(',')[1])
    expirationYear = int(expiration_date.split(',')[1])

    if entered_code != correct_code:
        return False

    elif (curentYear <= expirationYear and curentMonth == expirationMonth
          and curentDay <= expirationDay) or (curentYear <= expirationYear and
                                              curentMonth < expirationMonth):
        return True
    else:
        return False


print(check_coupon("123", "123", "July 00, 0000", "July 00, 0001"))
print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))
print(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014'))
print(check_coupon('123a', '123', 'September 5, 2014', 'October 1, 2014'))
