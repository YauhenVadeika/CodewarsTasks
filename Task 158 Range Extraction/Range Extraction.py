# my task solution
def solution(args):

    lst = []
    ptr = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == ptr:
                lst.append(str(ptr))
            elif end == ptr + 1:
                lst.extend([str(ptr), str(end)])
            else:
                lst.append(str(ptr) + "-" + str(end))
            ptr = n
        end = n

    return ",".join(lst)


print(
    solution([
        -10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15,
        17, 18, 19, 20
    ]))

# "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"


# codewars task best solution
def solution(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b + 1:
            ranges.append(
                str(a) if a ==
                b else "{}{}{}".format(a, "," if a + 1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)


# codewars task best solution
def solution(args):
    result = ""
    i = 0
    while i < len(args):
        val = args[i]
        while i + 1 < len(args) and args[i] + 1 == args[i + 1]:
            i += 1
        if val == args[i]:
            result += ",%s" % val
        elif val + 1 == args[i]:
            result += ",%s,%s" % (val, args[i])
        else:
            result += ",%s-%s" % (val, args[i])
        i += 1
    return result.lstrip(",")


# codewars task best solution
def solution(args):
    output = ''
    for n in args:
        if n == max(args): output += str(n)
        elif n + 1 not in args or (n - 1 not in args and n + 2 not in args):
            output += str(n) + ','
        elif n - 1 not in args:
            output += str(n) + '-'
    return output