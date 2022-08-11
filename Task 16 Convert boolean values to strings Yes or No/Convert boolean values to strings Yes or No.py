# My ideas
# a = False
# if a  == True:
#     print('Yes')
# else:
#     print('No')


# my task solution
def bool_to_word(boolean):
    return 'Yes' if boolean is True else 'No'


print(bool_to_word(True))
print(bool_to_word(False))


# codewars task best solution
def bool_to_word(bool):
    return "Yes" if bool else "No"


# codewars task best solution
def bool_to_word(bool):
    if bool:
        return "Yes"
    return "No"


# codewars task best solution
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
