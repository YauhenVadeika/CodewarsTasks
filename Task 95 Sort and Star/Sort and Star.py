# my task solution
def two_sort(array):
    return '***'.join((sorted(array))[0])


print(
    two_sort([
        "bitcoin", "take", "over", "the", "world", "maybe", "who", "knows",
        "perhaps"
    ]))
print(
    two_sort([
        "turns", "out", "random", "test", "cases", "are", "easier", "than",
        "writing", "out", "basic", "ones"
    ]))
print(
    two_sort(
        ["lets", "talk", "about", "javascript", "the", "best", "language"]))


# codewars task best solution
def two_sort(lst):
    return '***'.join(min(lst))


# codewars task best solution
def two_sort(a):
    a = sorted(a)
    result = "***".join(a[0])
    return result