
board = [list(map(int, input().split())) for _ in range(9)]
zero = [[i, j] for i in range(9) for j in range(9) if not board[i][j]]
flag = False


def getCandidates(row, col):
    candidates = set()
    for i in range(3):
        for j in range(3):
            candidates.add(board[row][3*i+j])
            candidates.add(board[3*(row//3)+i][3*(col//3)+j])
            candidates.add(board[3*i+j][col])
    return [i for i in range(10) if i not in candidates]


def solution(i):
    global flag
    if flag:
        return
    if i == len(zero):
        flag = True
        for i in range(9):
            print(*board[i])
        return
    else:
        row, col = zero[i]
        candidates = getCandidates(row, col)
        for candidate in candidates:
            board[row][col] = candidate
            solution(i+1)
            board[row][col] = 0


solution(0)
