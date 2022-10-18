# my task solution
def solution(nums):
    return sorted(nums) if nums else []


print(solution(None))
print(solution([1, 2, 3, 10, 5]))
print(solution([]))


# codewars task best solution
def solution(nums):
    return sorted(nums or [])


# codewars task best solution
def solution(nums):
    try:
        return sorted(nums)
    except TypeError:
        return []