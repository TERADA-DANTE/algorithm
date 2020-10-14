import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a-1][b-1] = min(graph[a-1][b-1], c)


def solution(n, m, graph):
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    if j != k and i != k:
                        graph[j][k] = min(
                            graph[j][k], graph[j][i] + graph[i][k])
    answer = []
    for arr in graph:
        answer.append(
            ' '.join(list(map(lambda v: str(0) if v == float('inf') else str(v), arr))))
    return '\n'.join(answer)


print(solution(n, m, graph))
