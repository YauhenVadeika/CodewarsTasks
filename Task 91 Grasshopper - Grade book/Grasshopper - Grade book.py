# my task solution
def get_grade(s1, s2, s3):

    score = round((s1 + s2 + s3) / 3)

    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'


print(get_grade(95, 90, 93))
print(get_grade(100, 85, 96))
print(get_grade(60, 82, 76))
print(get_grade(0, 0, 0))


# codewars task best solution
def get_grade(s1, s2, s3):
    return {
        6: 'D',
        7: 'C',
        8: 'B',
        9: 'A',
        10: 'A'
    }.get((s1 + s2 + s3) / 30, 'F')


# codewars task best solution
def get_grade(*s):
    return 'FFFFFFDCBAA'[sum(s)//30]


# codewars task best solution
def get_grade(*grades):
    mean = sum(grades)/len(grades)
    for score, grade in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]:
        if mean >= score:
            return grade