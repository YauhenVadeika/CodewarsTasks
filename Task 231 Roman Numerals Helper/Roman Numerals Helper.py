# my task solution


class RomanNumerals:
    sym = [
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
    ]
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    @staticmethod
    def to_roman(number):
        result = ''
        pointer = 0
        while number:
            div = number // RomanNumerals.num[pointer]
            number %= RomanNumerals.num[pointer]
            while div:
                result += RomanNumerals.sym[pointer]
                div -= 1
            pointer += 1
        return result

    @staticmethod
    def from_roman(roman_numeral):
        result = 0
        for idx, val in enumerate(roman_numeral):
            first_num = RomanNumerals.num[RomanNumerals.sym.index(val)]
            second_num = RomanNumerals.num[RomanNumerals.sym.index(
                roman_numeral[idx +
                              1])] if idx + 1 != len(roman_numeral) else -1
            if first_num >= second_num:
                result += first_num
            else:
                result -= first_num
        return result


print(RomanNumerals.from_roman('I'), 1, 'I should == 1')

# codewars task best solution
import string
from collections import OrderedDict


class RomanNumerals:

    @classmethod
    def to_roman(self, num):
        conversions = OrderedDict([('M', 1000), ('CM', 900), ('D', 500),
                                   ('CD', 400), ('C', 100), ('XC', 90),
                                   ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
                                   ('V', 5), ('IV', 4), ('I', 1)])
        out = ''
        for key, value in conversions.iteritems():
            while num >= value:
                out += key
                num -= value
        return out

    @classmethod
    def from_roman(self, roman):
        conversions = OrderedDict([('CM', 900), ('CD', 400), ('XC', 90),
                                   ('XL', 40), ('IX', 9), ('IV', 4),
                                   ('M', 1000), ('D', 500), ('C', 100),
                                   ('L', 50), ('X', 10), ('V', 5), ('I', 1)])
        out = 0
        for key, value in conversions.iteritems():
            out += value * roman.count(key)
            roman = string.replace(roman, key, "")
        return out


# codewars task best solution
from collections import OrderedDict
import re

ROMAN_NUMERALS = OrderedDict([
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
])

DECIMAL_TO_ROMAN = [(v, k) for k, v in ROMAN_NUMERALS.items()]

ROMAN_RE = '|'.join(ROMAN_NUMERALS)


class RomanNumerals(object):

    @staticmethod
    def from_roman(roman):
        return sum(ROMAN_NUMERALS[d] for d in re.findall(ROMAN_RE, roman))

    @staticmethod
    def to_roman(decimal):
        result = []
        for number, roman in DECIMAL_TO_ROMAN:
            while decimal >= number:
                decimal -= number
                result.append(roman)
        return ''.join(result)


# codewars task best solution
class RomanNumerals:

    def to_roman(val):
        onesRoman = [
            "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"
        ]
        tensRoman = [
            "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"
        ]
        hundsRoman = [
            "", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"
        ]
        thousRoman = ["", "M", "MM", "MMM", "MMMM"]

        ones = onesRoman[val % 10]
        tens = tensRoman[val // 10 % 10]
        hunds = hundsRoman[val // 100 % 10]
        thous = thousRoman[val // 1000]

        return thous + hunds + tens + ones

    def from_roman(roman_num):
        out = 0
        mx = 0
        for cur in map(
                lambda c: {
                    'M': 1000,
                    'D': 500,
                    'C': 100,
                    'L': 50,
                    'X': 10,
                    'V': 5,
                    'I': 1
                }[c], roman_num[::-1]):
            if cur >= mx:
                out += cur
                mx = cur
            else:
                out -= cur

        return out


# codewars task best solution
class RomanNumerals:

    @staticmethod
    def from_roman(s):
        X = [dict(zip('MDCLXVI', (1e3, 500, 100, 50, 10, 5, 1)))[x] for x in s]
        return int(sum((x, -x)[x < y] for x, y in zip(X, X[1:])) + X[-1])

    @staticmethod
    def to_roman(i, o=' I II III IV V VI VII VIII IX'.split(' ')):
        r = lambda n: o[n] if n < 10 else ''.join(
            dict(zip('IVXLC', 'XLCDM'))[c] for c in r(n // 10)) + o[n % 10]
        return r(i)


# codewars task best solution
class RomanNumerals():

    def to_roman(num):
        R2M = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        string = ''
        for k, v in R2M.items():
            count = num // v
            num %= v
            string += count * k

        return string

    def from_roman(roman):
        R2M = {
            'M': 1000,
            'i': 900,
            'D': 500,
            'j': 400,
            'C': 100,
            'k': 90,
            'L': 50,
            'l': 40,
            'X': 10,
            'm': 9,
            'V': 5,
            'n': 4,
            'I': 1
        }
        roman = roman.replace('CM', 'i').replace('CD', 'j').replace(
            'XC', 'k').replace('XL', 'l').replace('IX',
                                                  'm').replace('IV', 'n')
        return sum(R2M[i] for i in roman)
