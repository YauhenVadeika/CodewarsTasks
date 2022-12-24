# my task solution
def check_exam(arr1, arr2):

    steck = []

    for i in range(len(arr2)):
        if arr1[i] == arr2[i]:
            steck.append(4)
        elif arr2[i] == "":
            steck.append(0)
        else:
            steck.append(-1)

    if sum(steck) > 0:
        return sum(steck)
    else:
        return 0


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_exam(["а", "а", "в", "б"], ["а", "а", "б", ""]))
print(check_exam(["а", "а", "б", "в"], ["а", "а", "б", "в"]))
print(check_exam(["b", "c", "b", "a"], ["", "a", "a", "c"]))


# codewars task best solution
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))


# codewars task best solution
def check_exam(arr1, arr2):
    score = 0
    for i in range(0, 4):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] == "" or arr2[i] == "":
            score += 0
        else:
            score -= 1

    return score if score >= 0 else 0


# codewars task best solution
def check_exam(arr1, arr2):
    score = 0

    for i in range(0, len(arr1)):
        if arr1[i] == arr2[i]:
            score = score + 4
        elif arr2[i] != "":
            score -= 1
    return max(score, 0)


# codewars task best solution
def check_exam(answers, solutions):
    return max(
        sum([0, -1, 4][(ans == sol) + (sol != '')]
            for ans, sol in zip(answers, solutions)), 0)
