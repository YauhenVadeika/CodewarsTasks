# my task solution
def wave(people):
    if len(people) == 0:
        return []
    else:
        people = people.lower()
        the_waves = []
        for i, j in enumerate(people):
            if j == " ":
                continue
            else:
                the_waves.append(people[:i] + people[i].upper() + people[i + 1:])
        return the_waves


print(wave("Two words"))
print(wave("hello"))


# codewars task best solution
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]


# codewars task best solution
def wave(words):
    result = []
    chars = list(words)
    for index, char in enumerate(chars):
        if char.isalpha():
            copy = chars[:]
            copy[index] = copy[index].upper()
            result.append(''.join(copy))
    return result