# my task solution
def delete_nth(order, max_e):
    for i in reversed(range(len(order))):
        if order.count(order[i]) > max_e:
            order.pop(i)
    return order


print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))


# codewars task best solution
def delete_nth(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans


# codewars task best solution
def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
        n = d.get(item, 0)
        if n < max_e:
            res.append(item)
            d[item] = n + 1
    return res

