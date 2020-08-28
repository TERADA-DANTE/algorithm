import math
from collections import deque
t = int(input())


def isPrime(i):
    for j in range(2, int(math.sqrt(i))+1):
        if not i % j:
            return False
    return True


primes = [isPrime(i) for i in range(1000, 10000)]


def solution(a, b, s):
    isVisited = dict()
    dq = deque([a])
    while dq:
        l = len(dq)
        for _ in range(l):
            q = dq.popleft()
            if q == b:
                return s
            isVisited[q] = True
            # 다음 후보만든다.
            next = []
            t = str(q)
            for i in range(4):
                for j in range(10):
                    n = int(t[0:i] + str(j) + t[i+1:])
                    if 1000 <= n < 10000 and primes[n-1000] and not isVisited.get(n):
                        next.append(n)
            dq += next
        s += 1


k = []
for _ in range(t):
    a, b = list(map(int, input().split()))
    k.append(solution(a, b, 0))
print('\n'.join(list(map(str, k))))
