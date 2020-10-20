from collections import deque
h, w, k = list(map(int, input().split()))
board = [[0]*w for _ in range(h)]
isVisited = [[None] * w for _ in range(h)]
cnt = 0
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def createBlock(x1, y1, x2, y2):
    start = [max(y1, y2), min(x1, x2)]
    end = [min(y1, y2), max(x1, x2)]
    for i in range(start[0]-end[0]):
        for j in range(end[1]-start[1]):
            board[i+h-start[0]][j+start[1]] = 1


def solution(board):
    global cnt
    answer = []
    for i in range(h):
        for j in range(w):
            if not isVisited[i][j] and not board[i][j]:
                cnt += 1
                subCnt = 1
                queue = deque([[i, j]])
                while queue:
                    r, c = queue.popleft()
                    isVisited[r][c] = True
                    for a, b in moves:
                        row, col = r+a, c+b
                        if 0 <= row < h and 0 <= col < w and not isVisited[row][col] and not board[row][col]:
                            isVisited[row][col] = True
                            subCnt += 1
                            queue.append([row, col])
                answer.append(subCnt)
    answer.sort()
    return str(cnt) + '\n' + ' '.join(list(map(str, answer)))


for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))
    createBlock(x1, y1, x2, y2)
print(solution(board))
