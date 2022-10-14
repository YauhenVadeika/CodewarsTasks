# my task solution
def sort_by_length(arr):
    return sorted(arr, key=len)


print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))
print(sort_by_length(["beg", "life", "i", "to"]))


# codewars task best solution
def sort_by_length(arr):
    arr.sort(key=len)  # key sorts them by parameter of choosing
    return arr


# codewars task best solution
def sort_by_length(arr):
    words = {}
    for word in arr:
        words[int(len(word))] = word
    return [words[key] for key in sorted(words.keys())]


# codewars task best solution
def sort_by_length(arr):
    arr.sort(key=lambda x: len(x), reverse=False)
    return arr
