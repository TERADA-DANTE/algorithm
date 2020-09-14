import time
n, k = list(map(int, input().split()))


def f(n):
    print(n)
    i = 1000000007
    t = n % i
    series = []
    while i != 1:
        series.append(i)
        if i % 2:
            i -= 1
        else:
            i = int(i//2)
    while series:
        s = series.pop()
        if s % 2:
            t = (t * n) % i
        else:
            t = (t * t) % i
    return t


def solution(n, k):
    factorials = [None, 1]
    for i in range(2, n+1):
        factorials.append((factorials[-1] * i) % 1000000007)
    a = factorials[n]
    b = f(factorials[k] * factorials[n-k])
    return b
# a^p = a (mod p)
# a^-1 = a%(p-2) (mod p)
# nCk % p = (n! % p * (k! x (n-k)! )^(p-2) % p) % p


print(solution(n, k))
