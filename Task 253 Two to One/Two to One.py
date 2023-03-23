# my task solution
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


print(longest("aretheyhere", "yestheyarehere"))


# codewars task best solution
def longest(s1, s2):
    return ''.join(sorted((set(s1 + s2))))


# codewars task best solution
def longest(s1, s2):
    # your code

    # Defining the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Concatenating the Two Given Strings
    s = s1 + s2

    # Declaring the Output Variable
    y = ""

    # Comparing whether a letter is in the string
    for x in alphabet:
        if x not in s:
            continue
        if x in s:
            y = y + x

    # returning the final output
    return y


# codewars task best solution
def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))


# codewars task best solution
def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))


# codewars task best solution
def longest(s1, s2):
    x = ''
    y = sorted(s1 + s2)

    for i in y:
        if i not in x:
            x += i

    return x  # your code


# codewars task best solution
def longest(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    return "".join(sorted(set1 | set2))


# codewars task best solution
def longest(s1, s2):
    freq = {}
    for c in list(s1):
        freq[c] = freq.get(c, 0) + 1
    for c in list(s2):
        freq[c] = freq.get(c, 0) + 1
    l = sorted([c for c in list(freq.keys())])
    return ''.join(l)