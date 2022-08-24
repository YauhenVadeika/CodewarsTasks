# my task solution
def solution(s):
    return "".join([" " + item if item.isupper() else item for item in s])


print(solution(("breakCamelCase")))


# codewars task best solution
def solution(s):
    final_string = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string
