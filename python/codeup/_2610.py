from collections import deque
board = [list(input()) for _ in range(10)]
col, row = list(map(int, input().split()))
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
isVisited = [[None] * 10 for _ in range(10)]
isReverse = [[None] * 10 for _ in range(10)]
color = board[row][col]
queue = deque([[row, col]])
isReverse[row][col] = True


def reverse(s):
    return '_' if s == '*' else '*'


if color == '_':
    while queue:
        i, j = queue.popleft()
        isVisited[i][j] = True
        for x, y in moves:
            if 0 <= i+x < 10 and 0 <= y+j < 10:
                if not isVisited[i+x][j+y] and board[i+x][j+y] == color:
                    queue.append([i+x, j+y])
                    isReverse[i+x][j+y] = True
    for i in range(10):
        for j in range(10):
            if isReverse[i][j]:
                board[i][j] = reverse(board[i][j])
    for i in range(10):
        print(''.join(board[i]))
else:
    for i in range(10):
        print(''.join(board[i]))
