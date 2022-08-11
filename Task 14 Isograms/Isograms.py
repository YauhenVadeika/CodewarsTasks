# my task solution
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)


# print(is_isogram("Aba"))


# my task solution
def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True


# print(is_isogram("Aba"))


# codewars task best solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))
