# my task solution
def positive_sum(arr):
    lst = []
    [lst.append(i) if i >= 0 else 0 for i in arr]
    return sum(lst)


print(positive_sum([1, -4, 7, 12]))
print(positive_sum([-1, 2, 3, 4, -5]))
print(positive_sum([-1, -2, -3, -4, -5]))
print(positive_sum([]))


# codewars task best solution
def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# codewars task best solution
def positive_sum(arr):
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum


# codewars task best solution
def positive_sum(arr):
    return sum(filter(lambda x: x > 0, arr))


# codewars task best solution
def positive_sum(list):
    answer = 0
    for numbers in list:
        if numbers > 0:
            answer += numbers
    return answer