# my task solution
def are_you_playing_banjo(name):

    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


name = "Rikke"
name = "martin"
print(are_you_playing_banjo(name))


# codewars task best solution
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo"


# codewars task best solution
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'


# codewars task best solution
def areYouPlayingBanjo(name):
    return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"
