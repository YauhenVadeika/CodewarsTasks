# my task solution
def fake_bin(x):
    return "".join(["0" if int(i) <= 4 else "1" for i in x])


print(fake_bin("45385593107843568") == "01011110001100111")
print(fake_bin("509321967506747") == "101000111101101")


# codewars task best solution
def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


# codewars task best solution
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result


# codewars task best solution
import string


def fake_bin(s):
    return s.translate(string.maketrans('0123456789', '0000011111'))