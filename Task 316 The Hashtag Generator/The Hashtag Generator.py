"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def generate_hashtag(s):
    arr = '#' + ''.join([i.title() for i in s.split()])
    return False if len(arr) > 140 or arr == "#" else arr


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag(""))


# codewars task best solution
def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output


# codewars task best solution
def generate_hashtag(s):
    ans = '#' + str(s.title().replace(' ', ''))
    return s and not len(ans) > 140 and ans or False


# codewars task best solution
def generate_hashtag(s):
    return '#' + s.strip().title().replace(' ',
                                           '') if 0 < len(s) <= 140 else False


# codewars task best solution
def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    return "#" + ''.join(x.capitalize() for x in s.split(' '))


# codewars task best solution
def generate_hashtag(s):
    s = s.split()
    if len(s) > 140 or not (s):
        return False
    ans = '#'
    for word in s:
        ans += word.title()
    if len(ans) > 140 or not (s):
        return False
    return ans


# codewars task best solution
def generate_hashtag(s):
    return '#' + ''.join([word.title() for word in s.split(' ')
                          ]) if s and len(s) <= 140 else False


# codewars task best solution
generate_hashtag = lambda d: (lambda b: d > '' < b == b[:139] and '#' + b)(
    d.title().replace(' ', ''))


# codewars task best solution
def generate_hashtag(s):
    if len(s) > 140 or not s: return False
    return '#' + ''.join(w.capitalize() for w in s.split())
