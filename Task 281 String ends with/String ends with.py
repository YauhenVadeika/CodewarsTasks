"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def solution(text, ending):
    return text[-len(ending):] == ending


print(solution("samurai", "ai"))
print(solution("ninja", "ja"))
print(solution("sumo", "omo"))
print(solution("spam", "eggs"))


# codewars task best solution
def solution(string, ending):
    return string.endswith(ending)


# codewars task best solution
def solution(string, ending):
    return ending in string[-len(ending):]


# codewars task best solution
def solution(string, ending):
    if string.endswith(ending):
        return True
    return False


# codewars task best solution
def solution(string, ending):
    # your code here...
    string1 = len(string) - len(ending)
    string2 = len(string) - string1
    string3 = string[string1:]
    if string3 == ending:
        return True
    else:
        return False


# codewars task best solution
def solution(string, ending):
    return string[-(len(ending))::] == ending
