def solution(m, n, puddles):
    [row, col] = [n, m]
    board = [None] * row
    for i in range(row):
        board[i] = [1] * col
    for c, r in puddles:
        board[r-1][c-1] = 0
    for i in range(row):
        for j in range(col):
            if j > 0 and i > 0 and board[i][j]:
                board[i][j] = board[i-1][j] + board[i][j-1]
    return board


print(solution(4, 3, [[2, 2], [3, 2]]))
