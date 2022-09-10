# my task solution
def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    return res


print(tribonacci([1, 1, 1], 10))
print(tribonacci([300, 200, 100], 0))
print(tribonacci([0.5, 0.5, 0.5], 30))


# codewars task best solution
def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


# codewars task best solution
def tribonacci(s, n):
    for i in range(3, n):
        s.append(s[i - 1] + s[i - 2] + s[i - 3])
    return s[:n]


# codewars task best solution
def tribonacci(signature, n):
    output = signature[:n]
    while len(output) < n:
        output.append(sum(output[-3:]))
    return output