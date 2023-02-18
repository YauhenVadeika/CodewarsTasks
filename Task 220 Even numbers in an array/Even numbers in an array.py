# my task solution
def even_numbers(arr, n):

    return (([i for i in arr[::-1] if i % 2 == 0])[:n])[::-1]


print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2))
print(even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1))
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


# codewars task best solution
def even_numbers(arr, n):
    return [i for i in arr if i % 2 == 0][-n:]


# codewars task best solution
def even_numbers(arr, n):
    return list(filter(lambda n: n % 2 == 0, arr))[-n:]


# codewars task best solution
def even_numbers(arr, n):
    result = []
    a = list(reversed(arr))
    for number in a:
        if n == 0:
            break
        if number % 2 == 0:
            result.append(number)
            n -= 1
    return list(reversed(result))


# codewars task best solution
from typing import List


def even_numbers(array: List[int], n: int) -> List[int]:
    """
    Get a new array of length number containing the last 
    even numbers from the original array (in the same order).
    """
    return [_ for _ in array if not _ % 2][-n:]


# codewars task best solution
def even_numbers(arr, n):
    s = [num for num in arr if num % 2 == 0]
    return s[-n:]