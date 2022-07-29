# my task solution
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


print(greet('Daniel', 'Daniel'))
print(greet('Greg', 'Daniel'))


# my task solution
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"


print(greet('Daniel', 'Daniel'))
print(greet('Greg', 'Daniel'))


# codewars task best solution
def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"
