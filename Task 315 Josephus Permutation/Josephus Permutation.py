"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def josephus(items, k):

    sortarr = []
    n = 0

    while len(items) > 0:
        n = (n + k - 1) % len(items)
        sortarr.append(items[n])
        items.pop(n)

    return sortarr


print(josephus([1, 2, 3, 4, 5, 6, 7], 3))  # -- > [3, 6, 2, 7, 5, 1, 4]
print(josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4))
# # --> ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']
print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))


# codewars task best solution
def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys


# codewars task best solution
def josephus(n, k):
    i, ans = 0, []
    while n:
        i = (i + k - 1) % len(n)
        ans.append(n.pop(i))
    return ans


# codewars task best solution
class Circle(object):

    def __init__(self, items):
        self.items = items[:]

    def pop(self, index):
        norm_index = index % len(self.items)
        return self.items.pop(norm_index), norm_index

    def not_empty(self):
        return self.items


def josephus_iter(items, k):
    circle = Circle(items)
    i = k - 1  # index 0-based
    while circle.not_empty():
        item, i = circle.pop(i)
        yield item
        i += k - 1


def josephus(items, k):
    return list(josephus_iter(items, k))


# codewars task best solution
from collections import deque


def josephus(items, k):
    q = deque(items)
    return [[q.rotate(1 - k), q.popleft()][1] for _ in items]


# codewars task best solution
def josephus(items, k):
    out = []
    i = 0
    while len(items) > 0:
        i = (i + k - 1) % len(items)
        out.append(items[i])
        del items[i]
    return out


# codewars task best solution
def josephus(items, k):
    if len(items) == 0: return []
    if len(items) == 1: return [items[0]]
    i = ((k - 1) % len(items))
    return [items[i]] + josephus(items[i + 1:] + items[:i], k)


# codewars task best solution
def josephus(items, k):
    cursor = 0
    killed = []
    while len(items):
        cursor = (cursor + k - 1) % len(items)
        killed.append(items.pop(cursor))

    return killed