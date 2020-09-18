board = []
row, col = 1, 1
for _ in range(10):
    board.append(list(map(int, input().split())))
while True:
    if board[row][col] == 2:
        board[row][col] = 9
        break
    elif col < 9 and board[row][col+1] != 1:
        board[row][col] = 9
        col += 1
    elif row < 9 and board[row+1][col] != 1:
        board[row][col] = 9
        row += 1
    else:
        if not board[row][col]:
            board[row][col] = 9
        break
for i in range(10):
    print(*board[i])
