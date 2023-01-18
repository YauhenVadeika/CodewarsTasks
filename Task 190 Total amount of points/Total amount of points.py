# my task solution
def points(games):
    array = []
    for i in games:
        if int(i[0]) > int(i[-1]):
            array.append(3)
        elif int(i[0]) == int(i[-1]):
            array.append(1)
        else:
            array.append(0)
    return sum(array)


print(
    points(
        ['1:0', '2:3', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2',
         '4:3']))


# codewars task best solution
def points(a):
    return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))


# codewars task best solution
def points(games):
    count = 0
    for score in games:
        res = score.split(':')
        if res[0] > res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


# codewars task best solution
def points(games):
    result = 0
    for item in games:
        result += 3 if item[0] > item[2] else 0
        result += 1 if item[0] == item[2] else 0
    return result


# codewars task best solution


def points(games):
    return sum(3 if x > y else 0 if x < y else 1
               for x, y in (score.split(":") for score in games))


# codewars task best solution
def points(games):
    return sum([0, 1, 3][1 + (g[0] > g[2]) - (g[0] < g[2])] for g in games)


# codewars task best solution
points = lambda g: sum((x > y) * 3 or x == y for x, _, y in g)
