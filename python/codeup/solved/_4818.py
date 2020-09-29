n, m, k = list(map(int, input().split()))
board = [[1]*m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        board[i][j] = board[i-1][j] + board[i][j-1]
if not k:
    print(board[-1][-1])
else:
    row, col = int((k-1)//m), (k-1) % m
    board2 = [[1]*(m-col) for _ in range(n-row)]
    for i in range(1, len(board2)):
        for j in range(1, len(board2[0])):
            board2[i][j] = board2[i-1][j] + board2[i][j-1]
    print(board[row][col]*board2[-1][-1])
