# my task solution
def add_length(str_):
    return [f'{i} {str(len(i))}' for i in str_.split()]


print(add_length("apple ban"))
print(add_length("you will win"))


# codewars task best solution
def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]


# codewars task best solution
def add_length(str_):
    return [f"{w} {len(w)}" for w in str_.split()]


# codewars task best solution
def add_length(s):
    return ['%s %d' % (x, len(x)) for x in s.split()]


# codewars task best solution
def add_length(str_):
    answer = []
    for word in str_.split():
        answer.append(word + ' ' + str(len(word)))
    return answer

# codewars task best solution
add_length = lambda s: [f'{i} {str(len(i))}' for i in s.split()]