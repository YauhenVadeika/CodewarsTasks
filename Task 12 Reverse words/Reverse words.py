# My ideas
# text = "This is an example!"
# # text = "a b c d"
# lst = text[::-1]
# a = lst.split()
# b = a[::-1]
# c = " ".join(b)
# print(c)
# print(type(c))


# my task solution
def reverse_words(text):
    return ' '.join([x[::-1] for x in text.split(' ')])


print(reverse_words("This is an example!"))
print(reverse_words("a b c d"))
print(reverse_words("double  spaced  words"))


# codewars task best solution
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))


# codewars task best solution
def reverse_words(str):
    # go for it
    newStr = []
    for i in str.split(' '):
        newStr.append(i[::-1])
    return ' '.join(newStr)
