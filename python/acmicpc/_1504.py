import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, e = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(e):
    a, b, c = list(map(int, input().split()))
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])
v1, v2 = list(map(int, input().split()))


def daijkstra(x, graph):
    queue = [[x, 0]]
    lines = [0 if i == x else float('inf') for i in range(n)]
    while queue:
        idx, val = heappop(queue)
        for i, v in graph[idx]:
            if val+v < lines[i]:
                lines[i] = val+v
                heappush(queue, [i, val+v])
    return lines


def solution(n, e, graph):
    l = daijkstra(0, graph)
    a1 = l[v1-1]
    b1 = l[v2-1]
    l = daijkstra(v1-1, graph)
    c = l[v2-1]
    l = daijkstra(n-1, graph)
    a2 = l[v2-1]
    b2 = l[v1-1]
    answer = min(a1+a2+c, b1+b2+c)
    if answer == float('inf'):
        return -1
    return answer


print(solution(n, e, graph))
