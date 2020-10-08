n = int(input())
result = [None] * n
f = [1]
for i in range(n):
    f.append(f[-1]*(i+1))


def com(n, k):
    return int(f[n]/(f[k] * f[n-k]))


def pascal(n):
    result = [None] * (n+1)
    for i in range(n+1):
        result[i] = com(n, i)
    return result


for i in range(1, n+1):
    result[i-1] = pascal(i)
result.insert(0, [1])
for i in range(n):
    print(*result[i])
