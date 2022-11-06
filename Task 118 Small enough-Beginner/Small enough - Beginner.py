# my task solution
def small_enough(array, limit):
    return True if max(array) <= int(limit) else False


# codewars task best solution
def small_enough(array, limit):
    return max(array) <= limit


# codewars task best solution
def small_enough(array, limit):
    for e in array:
        if not e <= limit: return False
    return True
