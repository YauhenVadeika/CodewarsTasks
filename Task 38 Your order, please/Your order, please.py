# my task solution
def order(sentence):
    lst = []
    for n in range(1, 10):
        for item in sentence.split():
            if str(n) in item:
                lst.append(item)
    return " ".join(lst)


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))


# codewars task best solution
def order(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))
