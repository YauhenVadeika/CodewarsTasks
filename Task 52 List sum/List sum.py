# my task solution
def listsum(a, b):

    return [a[i] + b[i] for i in range(0, len(a))]


a = [1, 2, 3]
b = [6, 4, 0]

print(listsum(a, b))
