"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def is_pangram(s):

    return set([chr(i)
                for i in range(97, 123)]) - set([j
                                                 for j in s.lower()]) == set()


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
import string


def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())


# codewars task best solution
import string


def is_pangram(s):
    s = s.lower()
    for token in string.ascii_lowercase:
        if token not in s:
            return False
    return True


# codewars task best solution
def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(
        s.lower())) else False


# codewars task best solution
import string


def is_pangram(input_string):
    """Returns False if the input string is not a pangram else returns True"""
    return False if [
        char for char in string.ascii_lowercase
        if not char in input_string.lower()
    ] else True

    #I think this would be more readable
    '''
    for char in string.ascii_lowercase:
        if not char in input_string.lower():
            return False
    
    return True
    '''


# codewars task best solution
import string


def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwhyz'
    for letter in alphabet:
        if letter not in string.lower():
            return False
    return True