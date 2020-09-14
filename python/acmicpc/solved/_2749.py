n = int(input())
matrix = [[1, 1], [1, 0]]


def submul(arr):
    return sum(map(lambda v: (v[0] * v[1]) % 1000000, arr))


def mul(a, b):
    result = []
    for i in range(len(a)):
        temp = []
        for j in range(len(b)):
            temp.append(submul(zip(a[i], b[j])))
        result.append(temp)
    return result


def solution(n):
    series = []
    a = matrix
    while n != 1:
        series.append(n)
        if n % 2:
            n -= 1
        else:
            n = int(n//2)
    while series:
        s = series.pop()
        if s % 2:
            a = mul(a, list(zip(*matrix)))
        else:
            a = mul(a, list(zip(*a)))
    return a[0][1] % 1000000


print(solution(n))
