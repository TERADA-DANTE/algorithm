n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in range(n):
        board[i][j] += max([board[i+1][k] for k in range(n) if k != j])
