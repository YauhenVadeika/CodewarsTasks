# my task solution
def spin_words(sentence):
    c = []
    [c.append(i) if len(i) < 5 else c.append(i[::-1]) for i in list(sentence.split())]
    return " ".join(c)


print(spin_words("Welcome"))
print(spin_words("to"))
print(spin_words("Hey fellow warriors"))
print(spin_words("the string words"))


# codewars task best solution
def spin_words(sentence):   
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

# codewars task best solution
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

# codewars task best solution
def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())

# codewars task best solution
def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string