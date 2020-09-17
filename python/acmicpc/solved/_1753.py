from heapq import heappush, heappop
import sys
input = sys.stdin.readline
v, e = list(map(int, input().split()))


def solution(v, e):
    k = int(input())-1
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b, c = list(map(int, input().split()))
        graph[a-1].append([c, b-1])
    dist = [float('inf')] * v
    dist[k] = 0
    queue = [[0, k]]
    while queue:
        val, idx = heappop(queue)
        for v, i in graph[idx]:
            if val+v < dist[i]:
                dist[i] = val+v
                heappush(queue, [val+v, i])
    return '\n'.join(list(map(lambda v: "INF" if v == float('inf') else str(v), dist)))


print(solution(v, e))
