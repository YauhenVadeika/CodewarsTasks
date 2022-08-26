# my task solution
def alphabet_position(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(abc.find(item) + 1) for item in text.lower() if item in abc])


print(alphabet_position("The sunset sets at twelve o' clock."))

# dewars task best solution
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


# dewars task best solution
def alphabet_position(s):
    return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())


# dewars task best solution
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')