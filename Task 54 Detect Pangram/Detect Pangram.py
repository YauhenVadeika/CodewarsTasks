# my task solution
import string


def is_pangram(s):

    abc = set(string.ascii_lowercase)
    return set(s.lower()) >= abc


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))

# codewars task best solution
import string


def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


# codewars task best solution
def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(
        s.lower())) else False


# codewars task best solution
import string


def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
