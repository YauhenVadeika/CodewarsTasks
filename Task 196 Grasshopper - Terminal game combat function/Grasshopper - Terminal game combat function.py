# my task solution
def combat(health, damage):
    return f"{health-damage if health-damage > 0 else 0}"


print(combat(100, 5))
print(combat(83, 16))
print(combat(20, 30))


# my task solution
def combat(health, damage):
    if health - damage > 0:
        return health - damage
    return 0


print(combat(100, 5))
print(combat(83, 16))
print(combat(20, 30))


# codewars task best solution
def combat(health, damage):
    return max(0, health - damage)


# codewars task best solution
def combat(health, damage):
    return health - damage if health > damage else 0


# codewars task best solution
def combat(health, damage):
    return max(health - damage, 0)


# codewars task best solution
def combat(health, damage):
    if damage > health:
        return 0
    return health - damage


# codewars task best solution
def combat(health, damage):
    v = health - damage
    if v < 0:
        return 0
    else:
        return v