# my task solution
def descending_order(num):
    lst = [int(i) for i in str(num)]
    lst.sort(), lst.reverse()
    return int(''.join(map(str, lst)))


print(descending_order(123456789))
print(descending_order(145263))


# codewars task best solution
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


# codewars task best solution
def Descending_Order(num):
    if isinstance(num, int) and num >= 0:
        return int(''.join(sorted(str(num), reverse=True)))
    else:
        raise ValueError('Non-negative integer expected')
