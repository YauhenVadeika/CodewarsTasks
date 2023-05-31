"""Dear "good people" from the Codewars Team (P.I.O.R.Y).
I am very much concerned about your objectivity 
in the decisions you have made.
I keep moving on."""
"""You have not earned access to this kata's solutions
Solutions are locked for kata ranked far above your rank. 
Rank up or complete this kata to view the solutions. :)"""


# my task solution, my second life
def next_bigger(a):

    if a < 10:
        return -1

    b = [i for i in str(a)]
    # print(b)

    for j in reversed(range(len(b[:-1]))):
        for k in reversed(range(j, len(b))):
            if b[j] < b[k]:
                # print(b[j], b[k])
                b[j], b[k] = b[k], b[j]
                b[j + 1:] = sorted(b[j + 1:])
                return int(''.join(b))
    return -1


print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(5233))
print(next_bigger(1112))
print(next_bigger(2111))
print(next_bigger(5333))
print(next_bigger(9))
print(next_bigger(111))
print(next_bigger(531))
print(next_bigger(842665763092))

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


# codewars task best solution
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


# codewars task best solution
def next_bigger(n):
    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1
    a = n
    while True:
        a += 1
        if sorted(str(a)) == sorted(str(n)):
            return a


# codewars task best solution
def next_bigger(n):
    s = list(str(n))
    if s == sorted(s, reverse=True):
        return -1
    while True:
        n += 9
        if sorted(s) == sorted(list(str(n))):
            return n


# codewars task best solution
def next_bigger(n):
    prefix = list(str(n))
    postfix = [prefix.pop()]

    while prefix and prefix[-1] >= max(postfix):
        postfix.append(prefix.pop())

    if not prefix:
        return -1

    postfix.sort()
    i = next(i for i, d in enumerate(postfix) if d > prefix[-1])
    postfix[i], prefix[-1] = prefix[-1], postfix[i]
    return int(''.join(prefix + postfix))


# codewars task best solution
def next_bigger(n):
    cap = int(''.join(sorted(str(n), reverse=True)))
    if n == cap:
        return -1
    f = sorted(str(n))
    for c in range(n + 1, cap + 1):
        if sorted(str(c)) == f:
            return c


# codewars task best solution
def next_bigger(n):
    nums = list(str(n))
    length = len(nums) - 1
    suffix = length
    while nums[suffix - 1] >= nums[suffix] and suffix > 0:
        suffix -= 1
    if suffix <= 0:
        return -1

    rightmost = length
    while nums[rightmost] <= nums[suffix - 1]:
        rightmost -= 1
    nums[suffix - 1], nums[rightmost] = nums[rightmost], nums[suffix - 1]

    nums[suffix:] = nums[length:suffix - 1:-1]
    return int(''.join(nums))


# codewars task best solution
def next_bigger(number):
    number_list = list(str(number))
    if number_list == sorted(number_list, reverse=True):
        return -1
    if len(number_list) == 1:
        return number
    for i in range(len(number_list) - 2, -1, -1):
        for j in range(len(number_list) - 1, i, -1):
            if number_list[i] < number_list[j]:
                number_list[i], number_list[j] = number_list[j], number_list[i]
                number_list[i + 1:] = sorted(number_list[i + 1:])
                return int(''.join(number_list))


# codewars task best solution
def next_bigger(number):

    ##create a list of strings from the integer
    number = list(str(number))

    ##initialize an array stack-like object
    stack = []
    for i in range(len(number)):
        ##pop off the end of the array and store it as current
        current = number.pop()

        ##if the array is empty, just add it to the stack and move on
        if (len(stack) == 0):
            stack.insert(0, current)

        else:
            ##check to see if there are any integers in the stack that are less than the current number
            ## there is a lower number in the stack, get the index of the lowest number that is still lower than the current
            index = -1
            for j, s in enumerate(stack):
                if (current < s):
                    index = j
            ## if a lower number in the stack was spotted
            if (index > -1):
                swap = stack.pop(
                    index
                )  #remove the number at the index found above, store it as swap
                stack.append(current)  #add the current number to the stack
                stack.sort()  #sort the stack
                nextBigger = number + [
                    swap
                ] + stack  #combine the arrays in the new order
                return (int(''.join(nextBigger))
                        )  ##merge the array to an integer and return

            stack.insert(
                0, current
            )  ##add current number to stack if no lower numbers in the stack
    return (-1)  ##if there are no bigger numbers possible, return -1
