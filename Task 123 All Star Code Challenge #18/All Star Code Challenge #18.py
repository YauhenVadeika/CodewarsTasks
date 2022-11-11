# my task solution
def str_count(strng, letter):
    return strng.count(letter)


print(str_count("Hello", "o"))
print(str_count("Hello", "l"))
print(str_count("", "z"))


# codewars task best solution
def strCount(string, letter):
    return string.count(letter)


# codewars task best solution
def str_count(strng, letter):
    counter = 0
    
    for chr in strng:
        if chr == letter:
            counter += 1
        
    return counter