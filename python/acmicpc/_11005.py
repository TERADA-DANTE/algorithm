n, b = list(map(int, input().split()))


def underTen(n, b, m=[]):
    while n >= b:
        m = [n % b] + m
        n = n//b
    return [n % b] + m if m else [n]


def overTen(n, b, d, m=[]):
    while n >= b:
        m = [d[n % b]] + m
        n = n//b
    return [d[n % b]] + m if m else [d[n]]


def solution(n, b):
    if b < 10:
        return ''.join(map(str, underTen(n, b)))
    elif b == 10:
        return n
    d = dict()
    for i in range(b+1):
        if i < 10:
            d[i] = i
        else:
            d[i] = chr(i+55)
    return ''.join(map(str, overTen(n, b, d)))


print(solution(n, b))
