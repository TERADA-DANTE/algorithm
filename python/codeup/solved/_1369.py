n, k = list(map(int, input().split()))
board = [[' '] * n for _ in range(n)]

for i in range(n):
    board[i][-1] = '*'
    board[i][0] = '*'
    board[0][i] = '*'
    board[-1][i] = '*'
for i in range(n):
    for j in range(n):
        r = (i) % k + (j) % k
        if not (r+1) % k:
            board[i][j] = '*'
        #     0 1 2
        #     1 2 0
        #     2 0 1
        # 2 20 21 22 1 0 2
for i in range(n):
    print(''.join(board[i]))
