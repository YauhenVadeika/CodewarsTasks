# my task solution
def reverse(st):

    return " ".join(st.split()[::-1])
    # return " ".join(st.rstrip().split(" ")[::-1])


print(reverse('Hi There.'))
print(reverse('Hello World'))
print(reverse('dykpirpwu alwqqqigwuuhfeyswiaikeoaphrrdsod  ljhghdwfsh'))
print(reverse('kghpjsjhts fdse kh'))
print(
    reverse(
        'pgqeutgq  lsyodjti hygwhjfjplklrwktqiteafsgyaqkdorkjdograweqloqwjkhgjdagp'
    ))


# codewars task best solution
def reverse(st):
    return " ".join(reversed(st.split())).strip()


# codewars task best solution
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)


# codewars task best solution
def reverse(stg):
    return ' '.join(reversed(stg.split()))


# codewars task best solution
def reverse(st):
    return " ".join(st.split(" ")[::-1]).strip().replace("  ", " ").replace(
        "  ", " ")


# codewars task best solution
reverse = lambda _: ' '.join(filter(bool, _.strip().split(' ')[::-1]))
