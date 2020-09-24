n, k = list(map(int, input().split()))
d = dict({1: 1})


def factorials(n):
    if d.get(n):
        return d[n]
    d[n] = n*factorials(n-1)
    return d[n]


print(int(factorials(n)/(factorials(k)*factorials(n-k))))
