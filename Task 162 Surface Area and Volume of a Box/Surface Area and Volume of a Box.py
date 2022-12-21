# my task solution
def get_size(w, h, d):

    return [2 * (h * w) + 2 * (h * d) + 2 * (w * d), w * h * d]


print(get_size(4, 2, 6))


# codewars task best solution
def get_size(w, h, d):
    area = 2 * (w * h + h * d + w * d)
    volume = w * h * d
    return [area, volume]


# codewars task best solution
def get_size(w, h, d):
    ans = []
    surface = 2 * ((w * h) + (d * h) + (w * d))
    volume = w * h * d
    ans.append(surface)
    ans.append(volume)
    return ans
