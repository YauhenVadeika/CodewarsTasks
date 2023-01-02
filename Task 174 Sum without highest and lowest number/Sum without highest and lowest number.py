# my task solution
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0


print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([-6, -20, -1, -10, -12]))
print(sum_array([3]))
print(sum_array([-3]))
print(sum_array([-3]))
print(sum_array([3, 5]))
print(sum_array([-3, -5]))
print(sum_array(None))


# codewars task best solution
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


# codewars task best solution
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


# codewars task best solution
def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])


# codewars task best solution
def sum_array(arr):
    return sum(sorted(arr or [])[1:-1])