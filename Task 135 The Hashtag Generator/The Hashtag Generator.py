# my task solution
def generate_hashtag(s):

    return False if s == "" or len(
        s) > 140 else f"#{s.strip().title().replace(' ', '')}"


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))
print(generate_hashtag('Codewars Is Nice'))


# codewars task best solution
def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output


# codewars task best solution
def generate_hashtag(s):
    return '#' + s.strip().title().replace(' ',
                                           '') if 0 < len(s) <= 140 else False


# codewars task best solution
def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    return "#" + ''.join(x.capitalize() for x in s.split(' '))
