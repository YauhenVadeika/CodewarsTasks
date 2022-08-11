# my task solution
def get_count(sentence):
    vowels = "aeiou"
    return sum(item in vowels for item in sentence)


print(get_count("abracadabra"))
print(get_count(""))
print(get_count("y"))
print(get_count("aeiou"))


# codewars task best solution
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


# codewars task best solution
def getCount(s):
    return sum(c in 'aeiou' for c in s)
