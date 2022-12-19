# my task solution
def remove_smallest(numbers):
    
    if numbers == []:
        return []
    else:
        num = numbers.copy()
        num.remove(min(numbers))
        return num


print(remove_smallest([1, 2, 3, 4, 5]))
print(remove_smallest([2, 2, 1, 2, 1]))
print(remove_smallest([]))


# codewars task best solution
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


# codewars task best solution
def remove_smallest(numbers):
    if len(numbers) < 1: 
        return numbers
    idx = numbers.index(min(numbers))
    return numbers[0:idx] + numbers[idx+1:]


# codewars task best solution
def remove_smallest(n):
    return n[:n.index(min(n))] + n[n.index(min(n)) + 1:] if n != [] else []