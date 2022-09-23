# my task solution
def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if len(arr) != 0 else []


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))


# codewars task best solution
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
        if x > 0:
            pos += 1
        if x < 0:
            neg += x
    return [pos, neg]


# codewars task best solution
def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


# codewars task best solution
def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(
        y for y in arr if y < 0)] if arr else []

# codewars task best solution
def count_positives_sum_negatives(arr):
    output = []
    if arr:
        output.append(sum([1 for x in arr if x > 0]))
        output.append(sum([x for x in arr if x < 0]))
    return output