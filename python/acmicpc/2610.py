from collections import deque
n = int(input())
k = int(input())
lines = [list(map(int, input().split())) for _ in range(k)]


def solution(n, lines):
    # floyd-washall
    graph = [[] * n for _ in range(n)]
    board = [[float('inf') if i != j else 0
              for i in range(n)]for j in range(n)]
    for a, b in lines:
        board[a-1][b-1] = board[b-1][a-1] = 1
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                board[i][j] = min(board[i][k]+board[k][j], board[i][j])
    for i in range(n):
        for j in range(n):
            if board[i][j] == float('inf'):
                board[i][j] = 0
    isVisited = [None] * n
    result = []
    for i in range(n):
        history = []
        if isVisited[i]:
            continue
        queue = deque([i])
        isVisited[i] = True
        while queue:
            q = queue.popleft()
            history.append(q)
            for v in graph[q]:
                if not isVisited[v]:
                    isVisited[v] = True
                    queue.append(v)
        inf = float('inf')
        for h in sorted(history):
            if inf > sum(board[h]):
                inf = sum(board[h])
                ret = h+1
        result.append(ret)
    return str(len(result))+'\n' + '\n'.join(list(map(str, sorted(result))))


print(solution(n, lines))
