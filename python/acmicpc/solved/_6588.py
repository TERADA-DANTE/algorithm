import time
import sys

primes = [False, False] + [True] * (1000000-1)
for i in range(3, 1000001):
    if primes[i]:
        for j in range(i+i, 1000001, i):
            primes[j] = False


def solution(n):
    for i in range(3, n, 2):
        if primes[i] and primes[n-i]:
            return f'{n} = {i} + {n-i}'


while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    print(solution(n))
