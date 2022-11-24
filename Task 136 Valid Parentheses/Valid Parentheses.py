# my task solution
def valid_parentheses(string):

    box = 0
    for i in string:
        if i == '(':
            box += 1
        if i == ')':
            box -= 1
        if box < 0:
            return False
    return box == 0


print(valid_parentheses("(())((()())())"))
print(valid_parentheses(")(()))"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))  # --> False
print(valid_parentheses('y(pfisluxxrzun)htvkedx)nctkzrwrv(mzkr(ugz)oj')
      )  # --> True should equal False
print(valid_parentheses('())(()'))  # --> True should equal False


# codewars task best solution
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


# codewars task best solution
def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string:
        string = string.replace("()", "")
    return not string


# codewars task best solution
def valid_parentheses(string):

    stack = []
    for item in list(string):
        if item == '(':
            stack.append('(')
        elif item == ')':
            try:
                stack.pop()
            except:
                return False
    return len(stack) == 0