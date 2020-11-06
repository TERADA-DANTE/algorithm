from collections import deque
n = int(input())
t = int(input())
lines = [list(map(int, input().split())) for _ in range(t)]


def solution(n, lines):
    answer = [None] * n
    graphIn = [[] * n for _ in range(n)]
    graphOut = [[] * n for _ in range(n)]
    for a, b in lines:
        graphIn[b-1].append(a-1)
        graphOut[a-1].append(b-1)

    def BFS(i, graph, isVisited):
        queue = deque([i])
        while queue:
            q = queue.popleft()
            if not isVisited[q]:
                isVisited[q] = True
                for v in graph[q]:
                    queue.append(v)
        return isVisited

    for i in range(n):
        isVisitedIn = BFS(i, graphIn, [None]*n)
        isVisitedOut = BFS(i, graphOut, [None]*n)
        cnt = 0
        for j in range(n):
            if isVisitedIn[j] or isVisitedOut[j]:
                cnt += 1
        answer[i] = n-cnt
    return '\n'.join(list(map(str, answer)))


print(solution(n, lines))
