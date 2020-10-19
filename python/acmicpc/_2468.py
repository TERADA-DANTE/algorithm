import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# With DFS

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
Min = min([min(board[i]) for i in range(n)])
Max = max([max(board[i]) for i in range(n)])
answer = 0
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
isVisited = [[None] * n for _ in range(n)]


def dfs(p):
    cnt = 0

    def search(i, j, p):
        global isVisited
        isVisited[i][j] = True
        for r, c in moves:
            row, col = r+i, c+j
            if 0 <= row < n and 0 <= col < n and not isVisited[row][col] and board[row][col] > p:
                search(row, col, p)
        return

    for i in range(n):
        for j in range(n):
            if board[i][j] > p and not isVisited[i][j]:
                cnt += 1
                search(i, j, p)
    return cnt
    # i마다 dfs를 돌아 안전한 영역의 개수를 찾는다.


for p in range(Max+1):
    answer = max(answer, dfs(p))
    isVisited = [[None] * n for _ in range(n)]
print(answer)
