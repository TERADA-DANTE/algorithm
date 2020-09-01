from collections import deque


class Graph:
    def __init__(self, n):
        self.graph = [[None] * (n+1) for _ in range(n+1)]


n, m = list(map(int, input().split()))
cnt = 0


def BFS(i, graph):
    global cnt
    dq = deque([i])
    visited = []
    while dq:
        q = dq.popleft()
        if q not in visited:
            visited.append(q)
            dq += ([i for i in range(1, n+1) if graph[q][i]])
    cnt += 1
    return visited


def solution(n, m, history=[]):
    graph = Graph(n).graph
    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a][b] = graph[b][a] = True
    for i in range(1, n+1):
        if i not in history:
            history += BFS(i, graph)
    return cnt


print(solution(n, m))
