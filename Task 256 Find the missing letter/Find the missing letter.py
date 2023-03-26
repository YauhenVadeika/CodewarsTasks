# my task solution
def find_missing_letter(chars):
    box = chars[0]
    for i in range(1, len(chars)):
        if ord(chars[i]) - ord(chars[i - 1]) != 1:
            box = chr(ord(chars[i]) - 1)
    return box


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))


# codewars task best solution
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n + 1]) - 1:
        n += 1
    return chr(1 + ord(chars[n]))


# codewars task best solution
def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start + i]:
            return alphabet[start + i]


# codewars task best solution
def find_missing_letter(c):
    return next(
        chr(ord(c[i]) + 1) for i in range(len(c) - 1)
        if ord(c[i]) + 1 != ord(c[i + 1]))


# codewars task best solution
def find_missing_letter(chars):
    for x in range(1, len(chars)):
        if ord(chars[x]) - ord(chars[x - 1]) != 1:
            return chr(ord(chars[x]) - 1)


# codewars task best solution
def find_missing_letter(chars):
    return [
        chr(n) for n in range(ord(chars[0]),
                              ord(chars[-1]) + 1)
        if n not in [ord(c) for c in chars]
    ][0]


# codewars task best solution
def find_missing_letter(chars):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    match = False
    count = 0
    for letter in s:
        if letter == chars[count]:
            match = True
            count = count + 1
        elif match == True:
            return letter