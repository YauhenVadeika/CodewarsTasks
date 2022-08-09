# my task solution
def enough(cap, on, wait):
    if (on - wait) == 0 or (on + wait) - cap < 0:
        return 0
    else:
        return abs((on + wait) - cap)


# print(enough(10, 5, 5)) # -->0
# print(enough(100, 60, 50)) # -->10
# print(enough(20, 5, 5)) # -->0
print(enough(74, 17, 14))  # -->0


# codewars task best solution
def enough(cap, on, wait):
    return max(0, wait - (cap - on))


# codewars task best solution
def enough(cap, on, wait):
    return max(0, on + wait - cap)


# codewars task best solution
def enough(cap, on, wait):
    return wait + on - cap if wait + on > cap else 0


# codewars task best solution
def enough(cap, on, wait):
    return max(on + wait - cap, 0)
