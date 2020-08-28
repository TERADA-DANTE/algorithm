from collections import deque
t = int(input())


def solution(a, b):
    isVisited = dict({a: True})
    dq = deque([(a, '')])
    while dq:
        v, q = dq.popleft()
        if v == b:
            return q
        if not isVisited.get(v*2 % 10000):
            isVisited[v*2 % 10000] = True
            dq.append((v*2 % 10000, q+'D'))
        s = v-1 if v else 9999
        if not isVisited.get(s):
            isVisited[s] = True
            dq.append((s, q+'S'))
        l = int((v % 1000) * 10 + v / 1000)
        r = int((v % 10) * 1000 + v / 10)
        if not isVisited.get(l):
            isVisited[l] = True
            dq.append((l, q+'L'))
        if not isVisited.get(r):
            isVisited[r] = True
            dq.append((r, q+'R'))


k = []
for _ in range(t):
    a, b = list(map(int, input().split()))
    k.append(solution(a, b))
print('\n'.join(k))
