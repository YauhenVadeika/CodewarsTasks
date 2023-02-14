# my task solution
def is_anagram(test, original):
    return True if set(test.lower()) == set(
        original.lower()) and len(test) == len(original) else False


print(is_anagram("foefet", "toffee"))  # -- True
print(is_anagram("Buckethead", "DeathCubeK"))  # -- True
print(is_anagram("dumble", "bumble"))  #--> False
print(is_anagram("apple", "pale"))  # --> False


# codewars task best solution
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())


# codewars task best solution
from collections import Counter


# write the function is_anagram
def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())


# codewars task best solution
def is_anagram(test, original):
    test_dict, original_dict = {}, {}
    for i in test.lower():
        test_dict[i] = test_dict.get(i, 0) + 1
    for i in original.lower():
        original_dict[i] = original_dict.get(i, 0) + 1

    return test_dict == original_dict


# codewars task best solution
# write the function is_anagram
def is_anagram(test, original):
    if len(test) != len(original):
        return False

    alphabet = [0] * 26

    for i in range(len(test)):
        alphabet[(ord(test[i]) & 31) - 1] += 1
        alphabet[(ord(original[i]) & 31) - 1] -= 1

    return not any(alphabet)


# codewars task best solution
is_anagram = lambda t, o: sorted(t.lower()) == sorted(o.lower())