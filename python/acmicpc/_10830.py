n, b = list(map(int, input().split()))

matrix = [list(map(int, input().split())) for _ in range(n)]
series = []
while b != 1:
    series.append(b)
    b = int(b//2) if not b % 2 else b-1


def submul(arr):
    return sum(map(lambda v: v[0]*v[1], arr)) % 1000


def mul(a, b):
    result = []
    for i in range(len(a)):
        temp = []
        for j in range(len(b)):
            temp.append(submul(list(zip(a[i], b[j]))))
        result.append(temp)
    return result


def solution(series, a):
    while series:
        i = series.pop()
        if not i % 2:
            a = mul(a, list(zip(*a)))
        else:
            a = mul(a, list(zip(*matrix)))
    return '\n'.join(list(map(lambda v: ' '.join(list(map(lambda s: str(s % 1000), v))), a)))


print(solution(series, matrix))
