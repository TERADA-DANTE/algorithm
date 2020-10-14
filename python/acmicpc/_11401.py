
n, k = list(map(int, input().split()))


def solution(n, k):
    d = 1000000007
    factorials = [1, 1]
    for i in range(2, n+1):
        factorials.append((factorials[-1] * i) % d)
    a = factorials[n]

    b = (factorials[k] * factorials[n-k])
    t = d-2
    n = []
    while t != 1:
        n.append(t)
        if t % 2:
            t -= 1
        else:
            t = int(t//2)
    tail = b % d
    while n:
        m = n.pop()
        if m % 2:
            tail = (tail*b) % d
        else:
            tail = (tail*tail) % d
    return (a*tail) % d


# a^p % p = a (mod p)
# a^-1 = a%(p-2) (mod p)
# nCk % p = (n! % p / (k! x (n-k)! )^(p-2) % p) % p


print(solution(n, k))
