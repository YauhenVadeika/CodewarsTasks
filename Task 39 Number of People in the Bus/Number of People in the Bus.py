# my task solution
def number(bus_stops):
    a, b = 0, 0
    for i in bus_stops:
        a += i[0]
        b += i[1]
    return (a - b)


print(number([[10, 0], [3, 5], [5, 8]]))
print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))
print(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]))


# codewars task best solution
def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


# codewars task best solution
def number(stops):
    return sum(i - o for i, o in stops)


# codewars task best solution
def number(bus_stops):
    sum = 0
    for i in bus_stops:
        sum += i[0] - i[1]
    return sum