# my task solution
def queue_time(customers, n):
    lst = [0] * n
    for i in customers:
        lst[lst.index(min(lst))] += i
    return max(lst)


print(queue_time([1, 2, 3, 4, 5], 100))  # --> 5
print(queue_time([1, 2, 3, 4, 5], 1))  # --> 15
print(queue_time([5], 1))  # --> 5
print(queue_time([2, 2, 3, 3, 4, 4], 2))  # --> 9
print(queue_time([], 1))  # --> 0
print(queue_time([], 5))  # --> 0


# codewars task best solution
def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)


# codewars task best solution
def queue_time(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)