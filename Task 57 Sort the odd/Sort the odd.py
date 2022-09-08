# my task solution
def sort_array(source_array):
    odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]


print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


# codewars task best solution
def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]


# codewars task best solution
def sort_array(source_array):

    odds = []
    answer = []

    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")

        else:
            answer.append(i)

    odds.sort()

    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer
