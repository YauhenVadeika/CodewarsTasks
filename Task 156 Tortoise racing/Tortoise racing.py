# my task solution
def race(v1, v2, g):

    if v1 >= v2:
        return None
    else:
        time = g * 3600 / (v2 - v1)
        h = time / 3600
        mn = (time % 3600) / 60
        s = time % 60
    return [int(i) for i in [h, mn, s]]


print(race(720, 850, 70))
print(race(80, 91, 37))
print(race(820, 81, 550))

# codewars task best solution
from datetime import datetime, timedelta


def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g * 3600 / (v2 - v1))))
        d = datetime(1, 1, 1) + sec

        return [d.hour, d.minute, d.second]


# codewars task best solution
def race(v1, v2, g):
    t = 3600 * g / (v2 - v1)
    return [t / 3600, t / 60 % 60, t % 60] if v2 > v1 else None


# codewars task best solution
def race(v1, v2, g):
    if v2 > v1: return [(t := g / (v2 - v1) * 3600) // 3600, t // 60 % 60, int(t % 60)]
