# my task solution
def string_to_array(s):
    return s.split(" ")


print(string_to_array("Robin Singh"))
print(string_to_array("CodeWars"))
print(string_to_array("I love arrays they are my favorite"))


# codewars task best solution
def string_to_array(string=''):
    return string.split() if string else ['']


# codewars task best solution
def string_to_array(string):
    return string.split() or ['']


# codewars task best solution
string_to_array = lambda _: [__ for __ in _.split(' ')]
