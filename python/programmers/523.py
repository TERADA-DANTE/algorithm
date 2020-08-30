from collections import deque


def solution(N, road, K):
    [graph, isVisited] = [[[float('inf')] * N for _ in range(N)], [None] * N]
    for a, b, v in road:
        graph[a-1][b-1] = graph[b-1][a-1] = min(v, graph[a-1][b-1])

    dq = deque([[0, 0]])
    while dq:
        l = len(dq)
        t = []
        next = []
        for _ in range(l):
            i, v = dq.popleft()
            t.append(i)
            next += [[j, w+v]
                     for j, w in enumerate(graph[i]) if w+v <= K and not isVisited[j]]
        for k in t:
            isVisited[k] = True
        dq += next
    return isVisited.count(True)


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3
               ))
