# My ideas
# a = "aren't"
# b = a.title()
# c = a.capitalize()

# print(b)
# print(c)


# my task solution
def to_jaden_case(string):
    return ' '.join([i.capitalize() for i in string.split()])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# codewars task best solution
import string

toJadenCase = string.capwords


# codewars task best solution
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
