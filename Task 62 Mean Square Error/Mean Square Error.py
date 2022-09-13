# my task solution
def solution(array_a, array_b):
    return sum([((array_b[i] - array_a[i]) ** 2) for i in range(len(array_a))]) / len(array_a)


print(solution([1, 2, 3], [4, 5, 6]))
print(solution([10, 20, 10, 2], [10, 25, 5, -2]))


# codewars task best solution
def solution(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)


# codewars task best solution
from sklearn.metrics import mean_squared_error

def solution(array_a, array_b):
    return mean_squared_error(array_a,array_b)


# codewars task best solution
def solution(array_a, array_b):
    k=[]
    a=len(array_a)
    b=len(array_b)
    if a==b:
        for i in range(a):
            k.append((abs(array_a[i]-array_b[i])**2))
        l1=sum(k)
        r=l1/a
        return r