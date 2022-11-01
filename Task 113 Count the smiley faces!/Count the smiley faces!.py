# my task solution
def count_smileys(arr):
    count = 0
    for i in arr:
        if i in [
                ':D', ':)', ':-D', ':~D', ':-)', ':~)', ';D', ';)', ';-D',
                ';~D', ';-)', ';~)'
        ]:
            count += 1
    return count


print(count_smileys([]))
print(count_smileys([':D', ':~)', ';~D', ':)']))
print(count_smileys([':)', ';(', ';}', ':-D']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))

# codewars task best solution
from re import findall


def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


# codewars task best solution
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count


# codewars task best solution
def count_smileys(arr):
    smiles = set(
        [a + b + c for a in ":;" for b in ['', '-', '~'] for c in ")D"])
    return len([1 for s in arr if s in smiles])
