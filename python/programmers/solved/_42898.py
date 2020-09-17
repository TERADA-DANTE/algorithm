def solution(m, n, puddles):
    [row, col] = [n, m]
    board = [[1]*col for _ in range(row)]
    for c, r in puddles:
        board[r-1][c-1] = 0
    for i in range(row):
        for j in range(col):
            if not i and not j:
                pass
            elif board[i][j]:
                if not i:
                    board[i][j] = board[i][j-1]
                elif not j:
                    board[i][j] = board[i-1][j]
                else:
                    board[i][j] = (board[i-1][j]+board[i][j-1]) % 1000000007

    return board


print(solution(4, 3, [[1, 2], [2, 2]]))
