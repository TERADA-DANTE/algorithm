import time
from collections import deque
from heapq import heappush, heappop
n, k = list(map(int, input().split()))


def solution(n, k):
    dq = deque([i for i in range(1, n+1)])
    answer = []
    for _ in range(n):
        dq.rotate(-k+1)
        answer.append(dq.popleft())
    return '<' + ', '.join(map(str, answer)) + '>'


s = time.time()
print(solution(n, k))
print(time.time()-s)
