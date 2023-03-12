# my task solution
def rps(p1, p2):

    dictlst = {"rock": 1, "scissors": 2, "paper": 3}

    if dictlst[p1] == 3 and dictlst[p2] == 1:
        return "Player 1 won!"
    if dictlst[p1] == 1 and dictlst[p2] == 3:
        return "Player 2 won!"
    if dictlst[p1] < dictlst[p2]:
        return "Player 1 won!"
    if dictlst[p1] > dictlst[p2]:
        return "Player 2 won!"
    return 'Draw!'


print(rps('rock', 'scissors'))
print(rps('scissors', 'rock'))

print(rps('scissors', 'paper'))
print(rps('paper', 'scissors'))

print(rps('paper', 'rock'))
print(rps('rock', 'paper'))

print(rps('rock', 'rock'))


# codewars task best solution
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


# codewars task best solution
def rps(p1, p2):
    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


# codewars task best solution
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock'
          and p2 == 'scissors') or (p1 == 'scissors'
                                    and p2 == 'paper') or (p1 == 'paper'
                                                           and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'


# codewars task best solution
def rps(p1, p2):
    #your code here
    winner = {"scissors": "paper", "paper": "rock", "rock": "scissors"}
    if p1 == p2:
        return 'Draw!'
    elif winner[p1] == p2:
        return "Player 1 won!"
    elif winner[p2] == p1:
        return "Player 2 won!"


# codewars task best solution
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == 'rock' and p2 == 'scissors':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    else:
        return "Player 2 won!"


# codewars task best solution
def rps(p1, p2):
    d1 = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]
    return 'Draw!' if p1 == p2 else "Player {} won!".format(1 if (
        p1, p2) in d1 else 2)
