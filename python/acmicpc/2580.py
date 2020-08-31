board = [list(map(int, input().split())) for _ in range(9)]


def solution(board):
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                # 가로 확인
                check = [None] * 9
                for col in range(9):
                    if board[i][col]:
                        check[board[i][col]-1] = True
                if check.count(None) == 1:
                    board[i][j] = check.index(None) + 1
                    continue
                # 세로 확인
                check = [None] * 9
                for row in range(9):
                    if board[row][j]:
                        check[board[row][j]-1] = True
                if check.count(None) == 1:
                    board[i][j] = check.index(None) + 1
                    continue
                # 테두리 확인
                [r, c] = [3*(i//3), 3*(j//3)]
                check = [None] * 9
                for row in range(3):
                    for col in range(3):
                        if board[r+row][c+col]:
                            check[board[r+row][c+col]-1] = True
                if check.count(None) == 1:
                    board[i][j] = check.index(None) + 1
    return '\n'.join([' '.join(list(map(str, numbers))) for numbers in board])


print(solution(board))
