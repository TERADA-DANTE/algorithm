from collections import deque
n, m, v = list(map(int, input().split()))


def DFS(graph, v):
    dq = deque([v])
    history = []
    while dq:
        q = dq.pop()
        if q not in history:
            history.append(q)
            dq += list(reversed([i for i in range(n+1)
                                 if graph[q][i] and i not in history]))
    return ' '.join(map(str, history))


def BFS(graph, v):
    dq = deque([v])
    history = []
    while dq:
        q = dq.popleft()
        if q not in history:
            history.append(q)
            dq += [i for i in range(n+1) if graph[q][i] and i not in history]
    return ' '.join(map(str, history))


def solution(n, m, v):
    graph = [[None]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a][b] = True
        graph[b][a] = True
    return '\n'.join([DFS(graph, v), BFS(graph, v)])


print(solution(n, m, v))
