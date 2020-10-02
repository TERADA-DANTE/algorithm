from collections import deque
v, n = list(map(int, input().split()))
degrees = [0] * (v+1)
graph = [[None] * (v+1) for _ in range(v+1)]
degrees[0] = float('inf')
answer = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    degrees[b] += 1
    graph[a][b] = 1


def solution():
    queue = deque([i for i in range(1, v+1) if not degrees[i]])
    for i in range(1, v+1):
        if not queue:
            return 0
        q = queue.pop()
        answer.append(q)
        for j in range(1, v+1):
            if graph[q][j]:
                degrees[j] -= 1
                if not degrees[j]:
                    queue.append(j)
    return 1


t = solution()
if not t:
    print(-1)
else:
    for i in range(1, v+1):
        print(answer[i])
