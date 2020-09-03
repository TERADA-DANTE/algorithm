board = [list(map(int, input().split())) for _ in range(9)]
zero = [[i, j] for i in range(9) for j in range(9) if not board[i][j]]
flag = False


def solution(i):
    global flag, board, zero
    if flag:
        return board
    if i == len(zero):
        flag = True
        return board
    else:
        row, col = zero[i]


print(solution(0))
