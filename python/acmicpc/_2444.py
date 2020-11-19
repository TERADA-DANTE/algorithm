n = int(input())
board = [None] * n
for i in range(1, n+1):
    board[i-1] = ' ' * (n-i) + '*' * (2*i-1) + ' ' * (n-i)
board = board + list(reversed(board))[1:]
for i in range(2*n-1):
    print(board[i])
