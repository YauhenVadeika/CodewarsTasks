# my task solution
def validate_usr(username):
    for i in username:
        if i in " ":
            return False

    if len(username) < 3 or len(username) > 16:
        return False
    if username.islower():
        return True
    if username.count("_") > 3:
        return True
    return False


print(validate_usr('asddsa'))
print(validate_usr('____'))
print(validate_usr('a'))
print(validate_usr('_'))
print(validate_usr('1'))
print(validate_usr('Hass'))
print(validate_usr('asd43 34'))


# my task solution
def validate_usr(username):

    if len(username) < 3 or len(username) > 16 or " " in username:
        return False
    if username.islower():
        return True
    if username.count("_") > 3:
        return True
    return False


print(validate_usr('asddsa'))
print(validate_usr('____'))
print(validate_usr('a'))
print(validate_usr('_'))
print(validate_usr('1'))
print(validate_usr('Hass'))
print(validate_usr('asd43 34'))

# codewars task best solution
import re


def validate_usr(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None


# codewars task best solution
import re


def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))


# codewars task best solution
def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False
    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    for i in username:
        if i not in allowed:
            return False
    return True


# codewars task best solution
import re


def validate_usr(username):
    return re.match(r"^[a-z0-9_]{4,16}$", username) is not None


# codewars task best solution
def validate_usr(user):
    return 3 < len(user) < 17 and all(
        c in 'abcdefghijklmnopqrstuvwxyz_0123456789' for c in user)


# codewars task best solution
def validate_usr(username):
    numeric = "0123456789"
    if len(username) >= 4 and len(username) <= 16:
        for letter in username:
            status = 0
            if letter.islower() or letter == "_":
                status = 1
            for num in numeric:
                if letter == num:
                    status = 1
            if status == 0:
                return False
        return True
    else:
        return False