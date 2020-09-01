import sys
from collections import deque

input = sys.stdin.readline
col, row = list(map(int, input().split()))
steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
[board, isVisited] = [[], []]
for _ in range(row):
    board.append(list(map(int, input().split())))
    isVisited.append([False] * col)


def adjacent(i, j):
    candidates = []
    for k, l in steps:
        [a, b] = [i+k, j+l]
        if 0 <= a < row and 0 <= b < col and not board[a][b] and not isVisited[a][b]:
            isVisited[a][b] = True
            board[a][b] = 1
            candidates.append([a, b])
    return candidates


def solution(row, col, cnt=-1):
    initial = []
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                isVisited[i][j] = True
                initial.append([i, j])
    dq = deque(initial)
    while dq:
        l = len(dq)
        for _ in range(l):
            q = dq.popleft()
            dq += adjacent(*q)
        cnt += 1
    # 못만드는 경우
    for i in range(row):
        for j in range(col):
            if not board[i][j]:
                return -1
    return cnt


print(solution(row, col))
