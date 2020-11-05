from collections import deque
n = int(input())
t = int(input())
lines = [list(map(int, input().split())) for _ in range(t)]


def solution(n, lines):
    graph = [[] * n for _ in range(n)]
    for a, b in lines:
        graph[a-1].append(b-1)

    def BFS(i, cnt, isVisited):
        queue = deque([i])
        while queue:
            isVisited[i] = True
            cnt += 1
            for j in graph[i]:
                if not isVisited[j]:
                    queue.append()
    for i in range(n):
        print(BFS(i, 0, [None] * n))


print(solution(n, lines))
