"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def pig_it(text):
    return " ".join(
        [i[1:] + i[0] + "ay" if i.isalpha() else i for i in text.split(" ")])


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))


# codewars task best solution
def pig_it(text):
    lst = text.split()
    return ' '.join([
        word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst
    ])


# codewars task best solution
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x
                    for x in text.split())


# codewars task best solution
def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:] + i[0] + 'ay')
        else:
            res.append(i)

    return ' '.join(res)


# codewars task best solution
import re


def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)


# codewars task best solution
def pig_it(text):
    return ' '.join(
        [x[1:] + x[0] + 'ay' if x.isalpha() else x for x in text.split()])


# codewars task best solution
import re


def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)


# codewars task best solution
def pig_it(text):
    #your code here
    n = 0
    x = 0
    text = text.split()  #split the text into words
    text = list(text)  #make the words a list
    pig_text = []  #make an empty list
    for word in text:
        a = list(
            word)  #set a to be the list of word (the letters on their own)
        print(a)
        if len(a) > 1:
            a.append(a[0])  #add the first letter to the end
            del a[0]  #delete the first letter
            a.append('ay')  #add ay to the end
        if '!' in a:
            n += 1
        elif '?' in a:
            x += 1
        elif len(a) == 1:
            print(a)
            a.append('ay')
        a = ''.join(a)  #rejoin the word
        pig_text.append(a)  #put the word in the empty list
    pig_text = ' '.join(pig_text)  #join the words up with spaces
    return pig_text  #return the sentence


# codewars task best solution
def pig_it(text):
    piggy = []
    for word in text.split():
        if word.isalpha():
            piggy.append(word[1:] + word[0] + "ay")
        else:
            piggy.append(word)
    return ' '.join(piggy)


# codewars task best solution
def pig_it(text):
    return __import__("re").sub(
        r'\b\w+\b', lambda m: m.group(0)[1:] + m.group(0)[0] + 'ay', text)
