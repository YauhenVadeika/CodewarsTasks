# my task solution
def solution(string, ending):
    return True if string.endswith(ending) else False


print(solution('abc', 'bc'))
print(solution('abcde', 'abc'))
print(solution('abcde', ''))


# codewars task best solution
def solution(string, ending):
    return string.endswith(ending)


# codewars task best solution
def solution(string, ending):
    return ending in string[-len(ending):]
