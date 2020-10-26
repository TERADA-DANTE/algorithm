from collections import deque
row, col = list(map(int, input().split()))

board = [list(input()) for _ in range(row)]
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
answer = 0


def BFS(a, b):
    global answer
    isVisited = [[None] * col for _ in range(row)]
    queue = deque([[a, b, 0]])
    isVisited[a][b] = True
    while queue:
        r, c, cnt = queue.popleft()
        answer = max(answer, cnt)
        for x, y in moves:
            R, C = r+x, c+y
            if 0 <= R < row and 0 <= C < col and not isVisited[R][C] and board[R][C] == 'L':
                isVisited[R][C] = True
                queue.append([R, C, cnt+1])


def solution(row, col, board):
    # 모든점에서 BFS로 가장 먼거리 찾기 그리고 갱신
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'L':
                BFS(i, j)
    return answer


print(solution(row, col, board))
