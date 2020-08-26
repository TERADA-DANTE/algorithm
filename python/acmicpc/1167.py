import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

vertex = [None] + [None] * n
cost = dict()
arr = [None] + [[] for _ in range(n)]


def BFS(i):
    # 일단 BFS
    m = 0
    isVisited = [None] + [None] * n
    dq = deque([i])
    while dq:
        q = dq.popleft()
        if not isVisited[q]:
            isVisited[q] = True
            # i 방문 했으니 방문처리하고
            # i과 연결된 접점을 본다.
            t = 0
            for j in arr[q]:
                # 방문하지 않았다면 후보에 들어갈 수 있음
                if not isVisited[j]:
                    if t < cost[f'{q}{j}']:
                        t = cost[f'{q}{j}']
                        idx = j
                # 더이상 연결된 접점이 존재하지 않으면 탐색끝
            if not t:
                return m
            else:
                m += t
                dq.append(idx)


for _ in range(n):
    v, *d, _ = deque(list(map(int, input().split())))
    dq = deque(d)
    # dict에 n -> m의 경우 비용 저장 , 인접리스트 생성
    while dq:
        a = dq.popleft()
        b = dq.popleft()
        cost[f'{v}{a}'] = b
        arr[v].append(a)
# DFS로 다 돌면서 최대값 갱신
m = 0
for i in range(1, n+1):
    result = BFS(i)
    if m < result:
        m = result
print(m)
