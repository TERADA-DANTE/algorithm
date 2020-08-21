import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline


def DFS(i, j):
    if not 0 <= i < row or not 0 <= j < col:
        return
    if isVisited[i][j] or not board[i][j]:
        return
    isVisited[i][j] = True
    DFS(i, j+1)
    DFS(i-1, j+1)
    DFS(i-1, j)
    DFS(i-1, j-1)
    DFS(i, j-1)
    DFS(i+1, j-1)
    DFS(i+1, j)
    DFS(i+1, j+1)
    return


def solution(board, row, col, cnt=0):
    for i in range(row):
        for j in range(col):
            if not isVisited[i][j] and board[i][j]:
                DFS(i, j)
                cnt += 1
    return cnt


while True:
    col, row = list(map(int, input().split()))
    if not row:
        break
    [board, isVisited] = [[None] * row, [None] * row]
    for i in range(row):
        board[i] = list(map(int, input().split()))
        isVisited[i] = [None] * col
    print(solution(board, row, col))
