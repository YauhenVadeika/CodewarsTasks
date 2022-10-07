# my task solution
def no_space(x):
    return ''.join([i for i in x if i != " "])


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
print(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'))
print(no_space('8aaaaa dddd r     '))
print(no_space('jfBm  gk lf8hg  88lbe8 '))
print(no_space('8j aam'))

# my task solution
a = '8 j 8   mBliB8g  imjB8B8  jl  B'
print(a.replace(' ', ''))

# my task solution
a = '8 j 8   mBliB8g  imjB8B8  jl  B'
for i in a:
    if i != " ":
        print(i, end='')

# my task solution
a = '8 j 8   mBliB8g  imjB8B8  jl  B'
b = ''.join([i for i in a if i != " "])
print(b)


# codewars task best solution
def no_space(x):
    return x.replace(' ', '')


# codewars task best solution
def no_space(x):
    return "".join(x.split())


# codewars task best solution
no_space = lambda x: ''.join(x.split())