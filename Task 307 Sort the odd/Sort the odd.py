"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def sort_array(inarr):

    var = 0

    for i in range(len(inarr)):
        for j in range(len(inarr)):
            if inarr[i] % 2 != 0 and inarr[j] % 2 != 0:
                if inarr[i] < inarr[j]:
                    var = inarr[i]
                    inarr[i] = inarr[j]
                    inarr[j] = var
    return inarr


print(sort_array([7, 1]))
print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(
    sort_array([
        -43, -12, -16, -43, -40, -29, 22, 22, 36, -48, -38, -36, -17, 48, -3,
        1, 13, 46, 43, 43, 45, 32, -10, 47, 49, 16, 10, -6
    ])
)  # should equal [-43, -12, -16, -43, -40, -29, 22, 36, -48, -38, -36, -17, 48, -3, 1, 13, 46, 43, 22, 43, 45, 32, -10, 47, 49, 16, 10, -6]


# codewars task best solution
def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


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


# codewars task best solution
def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]


# codewars task best solution
def sort_array(source_array):
    odd = []
    for i in source_array:
        if i % 2 == 1:
            odd.append(i)
    odd.sort()
    x = 0
    for j in range(len(source_array)):
        if source_array[j] % 2 == 1:
            source_array[j] = odd[x]
            x += 1

    return source_array


# codewars task best solution
def sort_array(source_array):

    return [] if len(source_array) == 0 else list(
        map(int,
            (','.join(['{}' if a % 2 else str(a)
                       for a in source_array])).format(
                           *list(sorted(a for a in source_array
                                        if a % 2 == 1))).split(',')))


# codewars task best solution
def sort_array(source_array):
    odd = sorted(list(filter(lambda x: x % 2, source_array)))
    l, c = [], 0
    for i in source_array:
        if i in odd:
            l.append(odd[c])
            c += 1
        else:
            l.append(i)
    return l
