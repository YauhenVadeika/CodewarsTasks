# my task solution
def make_readable(time):

    if time >= 3600:
        ch = (time // 60) // 60
    else:
        ch = 0
    if ch >= 0:
        min = (time // 60) % 60
    else:
        min = 0
    if min >= 0:
        sec = (time % 3600000) % 60

    return f"{str(ch).zfill(2)}:{str(min).zfill(2)}:{(str(sec)).zfill(2)}"


print(make_readable(359999))
print(make_readable(86399))
print(make_readable(60))
print(make_readable(7))
print(make_readable(0))


# codewars task best solution
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


# codewars task best solution
def make_readable(seconds):
    hours, seconds = divmod(seconds, 60**2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


# codewars task best solution
def make_readable(seconds):
    h = seconds / 60**2
    m = (seconds % 60**2) / 60
    s = (seconds % 60**2 % 60)
    return "%02d:%02d:%02d" % (h, m, s)


# codewars task best solution
def make_readable(n):
    return f'{n//3600:02d}:{(n%3600)//60:02d}:{n%60:02d}'


# codewars task best solution
def make_readable(seconds):
    return "{0:02d}:{1:02d}:{2:02d}".format(seconds / 3600, seconds / 60 % 60,
                                            seconds % 60)
