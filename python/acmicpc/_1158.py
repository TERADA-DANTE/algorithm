import time
from collections import deque
n, k = list(map(int, input().split()))


def circularize(i):
    dq = deque()
    for i in range(1, n+1):
        dq.append(i)
    return dq


def solution(n, k):
    circle = circularize(n)
    i = 0
    answer = deque()
    while len(circle):
        if i+1 == k:
            answer.append(circle.popleft())
            i = -1
        else:
            circle.append(circle.popleft())
        i += 1
    return '<' + ', '.join(map(str, answer)) + '>'


s = time.time()
print(solution(n, k))
print(time.time()-s)
