import math
a, b = input().split()
d = dict()
for i in range(31):
    if i < 10:
        d[i] = i
    else:
        d[chr(i+55)] = i


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


def rnlcksgdk(n, b):
    if b < 10:
        return underTen(n, b)
    elif b == 10:
        return n
    d = dict()
    for i in range(b+1):
        if i < 10:
            d[i] = i
        else:
            d[i] = chr(i+55)
    return overTen(n, b, d)


def solution(a, b):
    n = int(input())
    numbers = input().split()
    dec = 0
    for i in range(n):
        dec += int(numbers[i])*math.pow(int(a), n-i-1)
    return rnlcksgdk(dec, int(b))


print(solution(a, b))
