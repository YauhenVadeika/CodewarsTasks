# my task solution
def data_reverse(data):

    box = []
    lst = [data[i:i + 8] for i in range(0, len(data), 8)][::-1]
    for j in lst:
        for k in j:
            box.append(k)
    return box


print(
    data_reverse([
        1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
        1, 0, 1, 0, 1, 0, 1, 0
    ]))


# codewars task best solution
def data_reverse(data):
    return sum([data[i - 8:i] for i in range(len(data), 0, -8)], [])


# codewars task best solution
def data_reverse(data):
    return data[-8:] + data_reverse(data[:-8]) if data else []


# codewars task best solution
def data_reverse(data):
    res = []

    for i in range(len(data) - 8, -1, -8):
        res.extend(data[i:i + 8])

    return res


# codewars task best solution
def data_reverse(data):
    return [b for a in xrange(len(data) - 8, -1, -8) for b in data[a:a + 8]]


# codewars task best solution
def blockify(data):
    result = []
    for i in range(0, len(data), 8):
        result.append(data[i:i + 8])
    return result


def unblockify(blocks):
    return [bit for block in blocks for bit in block]


def data_reverse(data):
    return unblockify(blockify(data)[::-1])


# codewars task best solution
def data_reverse(data):
    data2 = []
    j = len(data)
    while j > 0:
        data2 = data2 + data[j - 8:j]
        j = j - 8
    return data2


# codewars task best solution
def data_reverse(data):
    a, b, n = 0, 8, []
    while b <= len(data):
        n = data[a:b] + n
        a += 8
        b += 8
    return n


# codewars task best solution
def data_reverse(data):
    res = []
    while len(data) != 0:
        res += data[-8:]
        data = data[0:-8]
    return res