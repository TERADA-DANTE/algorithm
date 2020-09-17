

def solution(n, results):
    answer = []
    graph = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = float('inf')
    for a, b in results:
        graph[a-1][b-1] = 1
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
    for i in range(n):
        temp = []
        for j in range(n):
            if i != j and not (graph[i][j] == graph[j][i] == float('inf')):
                temp.append(j)
        if len(temp) == n-1:
            answer.append(i)
    return len(answer)


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
