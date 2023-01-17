# my task solution
def pipe_fix(nums):
    return list(range(nums[0], nums[-1] + 1))


print(pipe_fix([1, 3, 3, 5, 6, 7, 8]))


# codewars task best solution
def pipe_fix(num):
    return range(min(num), max(num) + 1)


# codewars task best solution
def pipe_fix(l):
    return [x for x in range(min(l), max(l) + 1)]


# codewars task best solution
def pipe_fix(arr):
    ls = []
    for i in range(arr[0], arr[len(arr) - 1] + 1):
        ls.append(i)
    return ls


# codewars task best solution
pipe_fix = lambda l: list(range(min(l), max(l) + 1))


# codewars task best solution
def pipe_fix(nums):
    nums.sort()
    new_list = []
    min = nums[0]
    max = nums[-1]
    while min <= max:
        new_list.append(min)
        min += 1
    return new_list