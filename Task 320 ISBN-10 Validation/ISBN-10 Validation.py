"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def valid_ISBN10(isbn):

    if (isbn.isdigit() or isbn.find('X') == 9) and len(isbn) == 10:

        return sum([
            int(index) * int(value) if value not in "X" else int(
                (value.replace('X', '10'))) * int(index)
            for index, value in enumerate(str(isbn), 1)
        ]) % 11 == 0
    else:
        return False


print(valid_ISBN10('1112223339'))  # --> True
print(valid_ISBN10('X123456788'))  # --> False
print(valid_ISBN10('048665088X'))  # --> True
print(valid_ISBN10('1112223339X'))  # --> False
print(valid_ISBN10('123456789T'))  # --> False
print(valid_ISBN10('ABCDEFGHIJ'))  # --> False
print(valid_ISBN10('XXXXXXXXXX'))  # --> False

# codewars task best solution
import re


def valid_ISBN10(isbn):
    return bool(re.match(
        "\d{9}[\dX]$", isbn)) and sum("0123456789X".index(d) * i
                                      for i, d in enumerate(isbn, 1)) % 11 == 0


# codewars task best solution
def valid_ISBN10(isbn):
    # Check format
    if len(isbn) != 10 or not (isbn[:-1].isdigit() and
                               (isbn[-1].isdigit() or isbn[-1] == 'X')):
        return False
    # Check modulo
    return sum(i * (10 if x == 'X' else int(x))
               for i, x in enumerate(isbn, 1)) % 11 == 0


# codewars task best solution
def valid_ISBN10(isbn):
    """
    Tests if string is a valid ISBN-10 identification.

    Parameters
    ----------
    isbn : str
        ISBN10 value to test.

    Returns
    -------
    bool
        Result, whether the string is a correct ISBN10.
    """

    isbn_lst = list(isbn)
    position = list(range(1, 11))
    allowed = list("0123456789X")
    num_lst = list()

    test = list(item for item in isbn_lst if item in allowed)
    if len(test) != 10:
        return False
    elif "X" in isbn and isbn.index("X") != 9:
        return False

    # Replaces "X" in "isbn_lst" if found.
    num_lst = list(10 if x == "X" else int(x) for x in isbn_lst)

    calc = sum(list(a * b for a, b in zip(num_lst, position))) % 11
    res = True if calc == 0 else False

    return res


# codewars task best solution
def valid_ISBN10(isbn: str) -> bool:
    try:
        digits = [
            *map(int, isbn[:-1]), 10 if isbn[-1] == 'X' else int(isbn[-1])
        ]
        return len(digits) == 10 and sum(
            int(c) * i for i, c in enumerate(digits, 1)) % 11 == 0

    except ValueError:
        return False


# codewars task best solution
def valid_ISBN10(s):
    n = s.replace(' ', '')
    return not sum((i + 1) * int((n[i], 10)[n[i] == 'X'])
                   for i in range(len(n))) % 11 and len(s) == 10 if s.rstrip(
                       'X').isdigit() else 0


# codewars task best solution
def valid_ISBN10(isbn):

    valid_chars = '0123456789X'

    if len(isbn) != 10: return False
    if 'X' in isbn[:9]: return False

    total = 0

    for index, char in enumerate(isbn):

        if char not in valid_chars:
            return False

        total += valid_chars.find(char) * (index + 1)

    return total % 11 == 0


# codewars task best solution
def valid_ISBN10(isbn):
    if set(isbn) <= set('0123456789X') and len(
            isbn) == 10 and 'X' not in isbn[:-1]:
        return sum(
            int(10 if j == 'X' else j) * i
            for i, j in enumerate(str(isbn), 1)) % 11 == 0
    else:
        return False


# codewars task best solution
def valid_ISBN10(isbn):
    if len(isbn) > 10 or all(i == 'X' for i in isbn): return False
    if len(isbn) == 10 and isbn.endswith('X'):
        return (int(isbn[0]) * 1 + int(isbn[1]) * 2 + int(isbn[2]) * 3 +
                int(isbn[3]) * 4 + int(isbn[4]) * 5 + int(isbn[5]) * 6 +
                int(isbn[6]) * 7 + int(isbn[7]) * 8 + int(isbn[8]) * 9 +
                10 * 10) % 11 == 0
    try:
        return (int(isbn[0]) * 1 + int(isbn[1]) * 2 + int(isbn[2]) * 3 +
                int(isbn[3]) * 4 + int(isbn[4]) * 5 + int(isbn[5]) * 6 +
                int(isbn[6]) * 7 + int(isbn[7]) * 8 + int(isbn[8]) * 9 +
                int(isbn[9]) * 10) % 11 == 0
    except:
        return False
