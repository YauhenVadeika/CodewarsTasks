# my task solution
def first_non_repeating_letter(string):
    reps = [c for c in string if string.lower().count(c.lower()) == 1]
    return reps[0] if len(reps) > 0 else ""


print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter(''))
print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter('aa'))
print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter('hello world, eh?'))
print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))


# codewars task best solution
def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]

    return ""


# codewars task best solution
def first_non_repeating_letter(string):
    for x in string:
        if string.lower().count(x.lower()) == 1:
            return x
    return ''


# codewars task best solution
def first_non_repeating_letter(string):
    return next((x for x in string if string.lower().count(x.lower()) == 1),
                '')


# codewars task best solution
def first_non_repeating_letter(string):
    return ([a for a in string if string.lower().count(a.lower()) == 1] or [''])[0]
