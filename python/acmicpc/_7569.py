import sys
from collections import deque
input = sys.stdin.readline
width, length, height = list(map(int, input().split()))

board = [[list(map(int, input().split())) for _ in range(length)]
         for _ in range(height)]
moves = [[0, 1, 0], [0, 0, 1], [0, -1, 0],
         [0, 0, -1], [1, 0, 0], [-1, 0, 0]]


def isValid(board):
    for i in range(height):
        for j in range(length):
            for k in range(width):
                if board[i][j][k] not in [1, -1]:
                    return False
    return True


def isUnavaliable(board):
    for i in range(height):
        for j in range(length):
            for k in range(width):
                if not board[i][j][k]:
                    # 모든 면이 -1로 되어있는경우
                    rounds = []
                    for h, l, w in moves:
                        z, y, x = h+i, w+k, l+j
                        if 0 <= z < height and 0 <= y < width and 0 <= x < length:
                            rounds.append(board[z][x][y])
                    if all([1 if round == -1 else 0 for round in rounds]):
                        return True
    return False


def solution(width, length, height, board):
    # 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
    cnt = 0
    if isValid(board):
        return cnt
    if isUnavaliable(board):
        return -1
    queue = deque()
    isVisited = [[[0] * width for _ in range(length)]
                 for _ in range(height)]
    for i in range(height):
        for j in range(length):
            for k in range(width):
                if board[i][j][k] == 1:
                    queue.append([i, j, k])
    while queue:
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            isVisited[z][x][y] = True
            for h, l, w in moves:
                a, b, c = z+h, x+l, y+w
                if 0 <= a < height and 0 <= b < length and 0 <= c < width and not isVisited[a][b][c] and not board[a][b][c]:
                    board[a][b][c] = 1
                    isVisited[a][b][c] = True
                    queue.append([a, b, c])
        cnt += 1
        if isValid(board):
            return cnt


print(solution(width, length, height, board))
