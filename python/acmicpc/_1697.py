import time
from collections import deque
n, k = list(map(int, input().split()))


def solution(n, k, s=0):
    if n >= k:
        return n-k
    isVisited = dict()
    dq = deque([n])
    while True:
        l = len(dq)
        for _ in range(l):
            q = dq.popleft()
            if q == k:
                return s
            if not isVisited.get(q):
                isVisited[q] = True
                if q-1 >= 0 and not isVisited.get(q-1):
                    dq.append(q-1)
                if q+1 < 100001 and not isVisited.get(q+1):
                    dq.append(q+1)
                if q*1 < 100001 and not isVisited.get(q*2):
                    dq.append(q*2)
        s += 1


# 5 17
# 4 6 10 5 4 6 10
# 3 8 7 9 11 20: 3 8 7 9 11 20 5 4 6 10
# 2


s = time.time()
print(solution(n, k))
print(time.time()-s)
