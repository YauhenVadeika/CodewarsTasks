# my task solution
def next_bigger(n):

    dig = [int(i) for i in str(n)]
    idn = len(dig) - 1
    while idn >= 1 and dig[idn - 1] >= dig[idn]:
        idn -= 1
    if idn == 0:
        return -1
    pivot = dig[idn - 1]
    swap_idn = len(dig) - 1
    while pivot >= dig[swap_idn]:
        swap_idn -= 1
    dig[swap_idn], dig[idn - 1] = dig[idn - 1], dig[swap_idn]
    dig[idn:] = dig[:idn - 1:-1]
    return int(''.join(str(n) for n in dig))


print(next_bigger(2017))
print(next_bigger(144))
print(next_bigger(21))
print(next_bigger(111))

# codewars task best solution
import itertools


def next_bigger(n):
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            t = s[i:]
            m = min(filter(lambda x: x > t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


# codewars task best solution
def next_bigger(n):
    # algorithm: go backwards through the digits
    # when we find one that's lower than any of those behind it,
    # replace it with the lowest digit behind that's still higher than it
    # sort the remaining ones ascending and add them to the end
    digits = list(str(n))
    for pos, d in reversed(tuple(enumerate(digits))):
        right_side = digits[pos:]
        if d < max(right_side):
            # find lowest digit to the right that's still higher than d
            first_d, first_pos = min(
                (v, p) for p, v in enumerate(right_side) if v > d)

            del right_side[first_pos]
            digits[pos:] = [first_d] + sorted(right_side)

            return int(''.join(digits))

    return -1


#codewars task best solution
def next_bigger(n):
    nums = list(str(n))
    for i in reversed(range(len(nums[:-1]))):
        for j in reversed(range(i, len(nums))):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = sorted(nums[i + 1:])
                return int(''.join(nums))
    return -1


# codewars task best solution
def next_bigger(n):
    n = str(n)[::-1]
    try:
        i = min(i + 1 for i in range(len(n[:-1])) if n[i] > n[i + 1])
        j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
        return int(n[i + 1::][::-1] + n[j] +
                   ''.join(sorted(n[j + 1:i + 1] + n[:j])))
    except:
        return -1


# codewars task best solution
def next_bigger(n):
    i, ss = n, sorted(str(n))

    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1

    while True:
        i += 1
        if sorted(str(i)) == ss and i != n:
            return i
