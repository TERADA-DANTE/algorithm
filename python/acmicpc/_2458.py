n, k = list(map(int, input().split()))
compares = [list(map(int, input().split())) for _ in range(k)]
inf = float('inf')


def solution(n, k, compares):
    graph = [[inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
    for a, b in compares:
        graph[a-1][b-1] = 1
    for k in range(n):
        for i in range(n):
            if i != k:
                for j in range(n):
                    if k != j:
                        graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            if not (graph[i][j] == inf and graph[j][i] == inf):
                temp.append(1)
        answer.append(temp)
    count = 0
    for arr in answer:
        if len(arr) == n:
            count += 1
    return count


print(solution(n, k, compares))
