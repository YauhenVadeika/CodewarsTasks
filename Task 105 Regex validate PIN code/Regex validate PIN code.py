# my task solution
def validate_pin(pin):
    return True if (len(pin) == 4 or len(pin) == 6) and pin.isdigit() else False


print(validate_pin("1234"))
print(validate_pin("0000"))
print(validate_pin("12345"))
print(validate_pin("а234"))
print(validate_pin("1.234"))
print(validate_pin("-12345"))
print(validate_pin("00000000"))


# codewars task best solution
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


# codewars task best solution
def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()


# codewars task best solution
validate_pin = lambda pin: len(pin) in (4, 6) and pin.isdigit()